import os
import sys
import argparse
from pathlib import Path

try:
    import pathspec
except ImportError:
    print("The 'pathspec' module is required for '--use-gitignore' functionality.")
    print("Install it using: pip install pathspec")
    sys.exit(1)

def load_gitignore_patterns(gitignore_path):
    with open(gitignore_path, 'r') as f:
        patterns = f.read().splitlines()
    spec = pathspec.PathSpec.from_lines('gitwildmatch', patterns)
    return spec

def tree(dir_path, prefix='', ignore_patterns=None, ignore_dirs_files=None, ignore_hidden=False, root_dir=None):
    if ignore_dirs_files is None:
        ignore_dirs_files = []
    lines = []
    # Update ignore_patterns if a .gitignore file exists in current directory
    gitignore_path = os.path.join(dir_path, '.gitignore')
    if os.path.exists(gitignore_path):
        ignore_patterns = load_gitignore_patterns(gitignore_path) if not ignore_patterns else ignore_patterns + load_gitignore_patterns(gitignore_path)
    try:
        contents = os.listdir(dir_path)
    except PermissionError:
        return lines
    contents = sorted(contents)
    if ignore_hidden:
        contents = [item for item in contents if not item.startswith('.')]
    # Filter out ignored directories and files
    contents = [item for item in contents if item not in ignore_dirs_files]
    # Apply .gitignore patterns
    if ignore_patterns:
        contents = [item for item in contents if not ignore_patterns.match_file(os.path.relpath(os.path.join(dir_path, item), start=root_dir))]
    pointers = ['├── '] * (len(contents) - 1) + ['└── '] if contents else []
    for pointer, item in zip(pointers, contents):
        item_path = os.path.join(dir_path, item)
        rel_path = os.path.relpath(item_path, start=root_dir)
        if ignore_patterns and ignore_patterns.match_file(rel_path):
            continue
        if os.path.isdir(item_path):
            lines.append(prefix + pointer + item + '/')
            extension = '│   ' if pointer == '├── ' else '    '
            lines.extend(tree(item_path, prefix=prefix + extension, ignore_patterns=ignore_patterns, ignore_dirs_files=ignore_dirs_files, ignore_hidden=ignore_hidden, root_dir=root_dir))
        else:
            lines.append(prefix + pointer + item)
    return lines

def main():
    parser = argparse.ArgumentParser(description='Generate a Markdown-formatted directory tree.')
    parser.add_argument('directory', help='The root directory to map.')
    parser.add_argument('-o', '--output', default='directory_structure.md', help='Output file name.')
    parser.add_argument('--ignore-git', action='store_true', help='Ignore the .git directory.')
    parser.add_argument('--ignore', nargs='*', default=[], help='List of directories or files to ignore.')
    parser.add_argument('--ignore-hidden', action='store_true', help='Ignore hidden files and directories.')
    parser.add_argument('--use-gitignore', action='store_true', help='Ignore files and directories specified in .gitignore.')
    args = parser.parse_args()

    dir_path = args.directory
    if not os.path.exists(dir_path):
        print(f'Error: Directory {dir_path} does not exist.')
        sys.exit(1)

    ignore_dirs_files = args.ignore
    if args.ignore_git:
        ignore_dirs_files.append('.git')

    # Load .gitignore patterns if --use-gitignore is set
    ignore_patterns = None
    if args.use_gitignore:
        gitignore_path = os.path.join(dir_path, '.gitignore')
        if os.path.exists(gitignore_path):
            ignore_patterns = load_gitignore_patterns(gitignore_path)
        else:
            print(f'Warning: .gitignore file not found in {dir_path}. Ignoring --use-gitignore flag.')

    dir_name = os.path.basename(os.path.abspath(dir_path))
    lines = [dir_name + '/']
    lines.extend(tree(dir_path, ignore_patterns=ignore_patterns, ignore_dirs_files=ignore_dirs_files, ignore_hidden=args.ignore_hidden, root_dir=dir_path))
    output = '\n'.join(lines)

    with open(args.output, 'w', encoding='utf-8') as f:
        f.write('```\n' + output + '\n```')

if __name__ == '__main__':
    main()
