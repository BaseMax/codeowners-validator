# CODEOWNERS Validator

A simple Python script to validate and check the existence of paths defined in a `.github/CODEOWNERS` file.

## Features

- Reads `.github/CODEOWNERS` file.
- Skips empty lines and comments.
- Extracts paths before the first `@` symbol.
- Checks if the paths exist in the repository.
- Outputs results with ✅ (exists) or ❌ (missing).

## Installation

Clone the repository:

```sh
git clone https://github.com/BaseMax/codeowners-validator.git
cd codeowners-validator
```

## Usage

Run the script from the root of your repository:

```sh
python codeowners_validator.py
```

## Requirements

- Python 3.x

## License

This project is licensed under the MIT License.

## Author

Copyright (c) 2025, Max Base.
