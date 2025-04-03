#
# Max Base
# https://github.com/BaseMax/codeowners-validator
#

import os
import argparse
import logging
from concurrent.futures import ThreadPoolExecutor

def setup_logging(log_file):
    """Configure logging settings."""
    logging.basicConfig(
        filename=log_file,
        level=logging.INFO,
        format="%(asctime)s - %(levelname)s - %(message)s",
    )

def get_valid_lines(file_path):
    """Read file and return valid lines (non-empty, non-comment)."""
    with open(file_path, "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip() and not line.startswith("#")]

def extract_paths(lines):
    """Extract paths from lines by taking text before first '@' and normalizing them."""
    return [line.split(" ")[0].lstrip("/") for line in lines]

def check_path_exists(path, base_dir, verbose=False):
    """Check if a given path exists and log the result."""
    full_path = os.path.join(base_dir, path)
    if os.path.exists(full_path):
        if verbose:
            logging.info(f"Checked {path}: Exists")
        return None
    else:
        status = f"❌ Missing: {path}"
        logging.info(status)
        return status

def check_paths_exist(paths, base_dir, exclude_dirs=None, verbose=False):
    """Check all extracted paths in parallel and exclude specific directories."""
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(lambda path: check_path_exists(path, base_dir, verbose), paths))

    for result in results:
        if result and (not exclude_dirs or not any(exclude in result for exclude in exclude_dirs)):
            print(result)

def main():
    """Main function to execute the script."""
    parser = argparse.ArgumentParser(description="Check if CODEOWNERS paths exist.")
    parser.add_argument("-f", "--file", default=".github/CODEOWNERS", help="Path to CODEOWNERS file")
    parser.add_argument("-d", "--dir", default=os.getcwd(), help="Project root directory")
    parser.add_argument("-e", "--exclude", nargs="*", default=[], help="List of directories/files to exclude from the check (e.g., docs/ tests/)")
    parser.add_argument("-v", "--verbose", action="store_true", help="Show detailed verbose output")
    parser.add_argument("-l", "--log", default="codeowners_check.log", help="Custom log file")
    args = parser.parse_args()

    setup_logging(args.log)

    if not os.path.exists(args.file):
        print("CODEOWNERS file not found!")
        return

    lines = get_valid_lines(args.file)
    paths = extract_paths(lines)
    check_paths_exist(paths, args.dir, exclude_dirs=args.exclude, verbose=args.verbose)

if __name__ == "__main__":
    main()
