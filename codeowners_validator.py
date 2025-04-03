#
# Max Base
# https://github.com/BaseMax/codeowners-validator
#

import os

def get_valid_lines(file_path):
    with open(file_path, "r", encoding="utf-8") as file:
        return [line.strip() for line in file if line.strip() and not line.startswith("#")]

def extract_paths(lines):
    return [line.split(" ")[0] for line in lines]

def check_paths_exist(paths, base_dir):
    for path in paths:
        full_path = os.path.join(base_dir, path.lstrip("/"))
        status = "✅ Exists" if os.path.exists(full_path) else "❌ Missing"
        print(f"{status}: {path}")

def main():
    codeowners_path = ".github/CODEOWNERS"
    project_root = os.path.abspath(os.path.dirname(__file__))
    
    if not os.path.exists(codeowners_path):
        print("CODEOWNERS file not found!")
        return
    
    lines = get_valid_lines(codeowners_path)
    paths = extract_paths(lines)
    check_paths_exist(paths, project_root)

if __name__ == "__main__":
    main()
