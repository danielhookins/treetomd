# Directory Tree to Markdown (treetomd.py)

A Python script to generate a Markdown-formatted directory tree of a given codebase or directory. This tool is especially useful for creating visual overviews of your project structure in README files or documentation.

       *
      ***
     *****
    *******
   *********
      | |
   TREE TO MD

## Table of Contents

- [Features](#features)
- [Requirements](#requirements)
- [Installation](#installation)
- [Usage](#usage)
  - [Basic Usage](#basic-usage)
  - [Options](#options)
  - [Examples](#examples)
- [Output Example](#output-example)
- [Notes](#notes)
- [License](#license)

---

## Features

- **Generate Directory Tree:** Recursively scans a directory and generates a tree structure.
- **Markdown Formatting:** Outputs the tree in Markdown code blocks for easy inclusion in documentation.
- **Ignore Specific Files/Directories:**
  - Use `--ignore` to specify files or directories to exclude.
  - Use `--ignore-git` to exclude the `.git` directory.
  - Use `--ignore-hidden` to exclude hidden files and directories.
- **Use `.gitignore` Patterns:**
  - Use `--use-gitignore` to ignore files and directories specified in `.gitignore` files.
  - Supports multiple `.gitignore` files in subdirectories.
- **Custom Output File Name:** Specify the output file name using `-o` or `--output`.
- **Cross-Platform Compatibility:** Works on Windows, macOS, and Linux.

---

## Requirements

- **Python 3.x**
- **pathspec Module** (required if using `--use-gitignore`)

  Install the `pathspec` module using pip:

  ```bash
  pip install pathspec
  ```

---

## Installation

1. **Clone or Download the Script:**

   Save the script as `treetomd.py` in your desired directory.

2. **Make the Script Executable (Optional):**

   On Unix-based systems (macOS, Linux), you can make the script executable:

   ```bash
   chmod +x treetomd.py
   ```

3. **Ensure Dependencies are Installed:**

   If you plan to use the `--use-gitignore` feature, install the `pathspec` module:

   ```bash
   pip install pathspec
   ```

---

## Usage

### Basic Usage

```bash
python treetomd.py <directory>
```

- `<directory>`: The root directory you want to map.

### Options

- `-h`, `--help`: Show help message and exit.
- `-o`, `--output`: Specify the output file name (default: `directory_structure.md`).
- `--ignore-git`: Ignore the `.git` directory.
- `--ignore`: Space-separated list of directories or files to ignore.
- `--ignore-hidden`: Ignore hidden files and directories (those starting with `.`).
- `--use-gitignore`: Ignore files and directories specified in `.gitignore` files.

### Examples

1. **Generate a Directory Tree of a Codebase:**

   ```bash
   python treetomd.py /path/to/your/codebase
   ```

2. **Ignore the `.git` Directory:**

   ```bash
   python treetomd.py /path/to/your/codebase --ignore-git
   ```

3. **Ignore Specific Directories or Files:**

   ```bash
   python treetomd.py /path/to/your/codebase --ignore node_modules dist build
   ```

4. **Ignore Hidden Files and Directories:**

   ```bash
   python treetomd.py /path/to/your/codebase --ignore-hidden
   ```

5. **Use `.gitignore` to Exclude Files and Directories:**

   ```bash
   python treetomd.py /path/to/your/codebase --use-gitignore
   ```

6. **Combine Multiple Options:**

   ```bash
   python treetomd.py /path/to/your/codebase --ignore-git --ignore-hidden --use-gitignore --ignore dist build
   ```

7. **Specify Output File Name:**

   ```bash
   python treetomd.py /path/to/your/codebase -o my_directory_tree.md
   ```

---

## Output Example

Assuming your project has the following structure:

```
/path/to/your/codebase/
├── .git/
├── .gitignore
├── README.md
├── src/
│   ├── main.py
│   ├── utils.py
│   ├── __pycache__/
│   └── .gitignore
├── tests/
│   ├── test_main.py
│   └── .DS_Store
├── build/
├── dist/
└── .env
```

And your `.gitignore` file contains:

```
# Root .gitignore
build/
dist/
.env
*.pyc

# src/.gitignore
__pycache__/
```

Running the script with `--use-gitignore --ignore-git --ignore-hidden`:

```bash
python treetomd.py /path/to/your/codebase --use-gitignore --ignore-git --ignore-hidden
```

**Generated `directory_structure.md`:**

````markdown
```
codebase/
├── README.md
├── src/
│   ├── main.py
│   └── utils.py
└── tests/
    └── test_main.py
```
````

---

## Notes

- **Dependencies:**
  - The `pathspec` module is required only if you use the `--use-gitignore` option. Install it via `pip install pathspec`.
- **Hidden Files and Directories:**
  - By default, hidden files and directories are included. Use `--ignore-hidden` to exclude them.
- **Multiple `.gitignore` Files:**
  - The script supports multiple `.gitignore` files in subdirectories. Patterns are applied recursively within their respective directories.
- **Permission Errors:**
  - The script gracefully handles permission errors by skipping directories that cannot be accessed.
- **Unicode Characters:**
  - The tree structure uses Unicode characters for better visual representation. Ensure your terminal or text editor supports UTF-8 encoding.
- **Cross-Platform:**
  - The script is compatible with Windows, macOS, and Linux.

---

## License

This script is released under the [MIT License](https://opensource.org/licenses/MIT).
