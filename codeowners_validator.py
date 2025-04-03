#
# Max Base
# https://github.com/BaseMax/codeowners-validator
#

import os
import argparse
import logging
from concurrent.futures import ThreadPoolExecutor

def setup_logging():
    """Configure logging settings."""
    logging.basicConfig(
        filename="codeowners_check.log",
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

def check_path_exists(path, base_dir):
    """Check if a given path exists and log the result."""
    full_path = os.path.join(base_dir, path)
    status = "✅ Exists" if os.path.exists(full_path) else "❌ Missing"
    logging.info(f"{status}: {path}")
    return f"{status}: {path}"

def check_paths_exist(paths, base_dir):
    """Check all extracted paths in parallel."""
    with ThreadPoolExecutor() as executor:
        results = list(executor.map(lambda path: check_path_exists(path, base_dir), paths))
    for result in results:
        print(result)

def main():
    """Main function to execute the script."""
    parser = argparse.ArgumentParser(description="Check if CODEOWNERS paths exist.")
    parser.add_argument("-f", "--file", default=".github/CODEOWNERS", help="Path to CODEOWNERS file")
    parser.add_argument("-d", "--dir", default=os.getcwd(), help="Project root directory")
    args = parser.parse_args()
    
    setup_logging()
    
    if not os.path.exists(args.file):
        print("CODEOWNERS file not found!")
        return
    
    lines = get_valid_lines(args.file)
    paths = extract_paths(lines)
    check_paths_exist(paths, args.dir)

if __name__ == "__main__":
    main()
    
