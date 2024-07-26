import json
import argparse

# subtask 1
def load_directory_structure(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def list_directory_contents(directory, all_files=False):
    contents = directory.get('contents', [])
    items = []

    for item in contents:
        if not all_files and item['name'].startswith('.'):
            continue
        items.append(item['name'])

    return items

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="List directory contents.")
    parser.add_argument('file', type=str, help="Path to the JSON file describing the directory structure.")
    parser.add_argument('-a', '--all', action='store_true', help="Do not ignore entries starting with .")
    
    args = parser.parse_args()
    
    # Load the directory structure
    directory_structure = load_directory_structure(args.file)
    
    # List the contents
    items = list_directory_contents(directory_structure, all_files=args.all)
    
    # Print the items
    print(" ".join(items))

if __name__ == "__main__":
    main()


#subtask 2

    

import json
import argparse

def load_directory_structure(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def list_directory_contents(directory, all_files=False, almost_all=False):
    contents = directory.get('contents', [])
    items = []

    for item in contents:
        if not almost_all and item['name'].startswith('.'):
            continue
        items.append(item['name'])

    return items

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="List directory contents.")
    parser.add_argument('file', type=str, help="Path to the JSON file describing the directory structure.")
    parser.add_argument('-a', '--all', action='store_true', help="Do not ignore entries starting with .")
    parser.add_argument('-A', '--almost-all', action='store_true', help="Include almost all entries, including .")
    
    args = parser.parse_args()
    
    # Load the directory structure
    directory_structure = load_directory_structure(args.file)
    
    # Determine which option to use
    if args.all:
        items = list_directory_contents(directory_structure, all_files=True)
    else:
        items = list_directory_contents(directory_structure, almost_all=args.almost_all)
    
    # Print the items
    print(" ".join(items))

if __name__ == "__main__":
    main()


#subtask 3

import json
import argparse
import time

def load_directory_structure(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def format_time(epoch_time):
    return time.strftime("%b %d %H:%M", time.localtime(epoch_time))

def list_directory_contents(directory, all_files=False, almost_all=False, long_format=False):
    contents = directory.get('contents', [])
    items = []

    for item in contents:
        if not almost_all and item['name'].startswith('.'):
            continue
        if long_format:
            permissions = item['permissions']
            size = item['size']
            time_modified = format_time(item['time_modified'])
            name = item['name']
            items.append(f"{permissions} {size} {time_modified} {name}")
        else:
            items.append(item['name'])

    return items

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="List directory contents.")
    parser.add_argument('file', type=str, help="Path to the JSON file describing the directory structure.")
    parser.add_argument('-a', '--all', action='store_true', help="Do not ignore entries starting with .")
    parser.add_argument('-A', '--almost-all', action='store_true', help="Include almost all entries, including .")
    parser.add_argument('-l', '--long', action='store_true', help="Use a long listing format")
    
    args = parser.parse_args()
    
    # Load the directory structure
    directory_structure = load_directory_structure(args.file)
    
    # Determine which option to use
    if args.all:
        items = list_directory_contents(directory_structure, all_files=True, long_format=args.long)
    else:
        items = list_directory_contents(directory_structure, almost_all=args.almost_all, long_format=args.long)
    
    # Print the items
    print("\n".join(items))

if __name__ == "__main__":
    main()


# subtask 4


import json
import argparse
import time

def load_directory_structure(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def format_time(epoch_time):
    return time.strftime("%b %d %H:%M", time.localtime(epoch_time))

def list_directory_contents(directory, all_files=False, almost_all=False, long_format=False, reverse=False):
    contents = directory.get('contents', [])
    items = []

    for item in contents:
        if not almost_all and item['name'].startswith('.'):
            continue
        if long_format:
            permissions = item['permissions']
            size = item['size']
            time_modified = format_time(item['time_modified'])
            name = item['name']
            items.append(f"{permissions} {size} {time_modified} {name}")
        else:
            items.append(item['name'])
    
    if reverse:
        items.reverse()

    return items

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="List directory contents.")
    parser.add_argument('file', type=str, help="Path to the JSON file describing the directory structure.")
    parser.add_argument('-a', '--all', action='store_true', help="Do not ignore entries starting with .")
    parser.add_argument('-A', '--almost-all', action='store_true', help="Include almost all entries, including .")
    parser.add_argument('-l', '--long', action='store_true', help="Use a long listing format")
    parser.add_argument('-r', '--reverse', action='store_true', help="Reverse the order of the listing")

    args = parser.parse_args()
    
    # Load the directory structure
    directory_structure = load_directory_structure(args.file)
    
    # Determine which options to use
    items = list_directory_contents(
        directory_structure, 
        all_files=args.all, 
        almost_all=args.almost_all, 
        long_format=args.long, 
        reverse=args.reverse
    )
    
    # Print the items
    print("\n".join(items))

if __name__ == "__main__":
    main()

#subtask 5


import json
import argparse
import time

def load_directory_structure(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def format_time(epoch_time):
    return time.strftime("%b %d %H:%M", time.localtime(epoch_time))

def list_directory_contents(directory, all_files=False, almost_all=False, long_format=False, reverse=False, sort_by_time=False):
    contents = directory.get('contents', [])
    items = []

    for item in contents:
        if not almost_all and item['name'].startswith('.'):
            continue
        if long_format:
            permissions = item['permissions']
            size = item['size']
            time_modified = format_time(item['time_modified'])
            name = item['name']
            items.append((item['time_modified'], f"{permissions} {size} {time_modified} {name}"))
        else:
            items.append((item['time_modified'], item['name']))
    
    if sort_by_time:
        items.sort(key=lambda x: x[0])
    
    if reverse:
        items.reverse()

    return [item[1] for item in items]

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="List directory contents.")
    parser.add_argument('file', type=str, help="Path to the JSON file describing the directory structure.")
    parser.add_argument('-a', '--all', action='store_true', help="Do not ignore entries starting with .")
    parser.add_argument('-A', '--almost-all', action='store_true', help="Include almost all entries, including .")
    parser.add_argument('-l', '--long', action='store_true', help="Use a long listing format")
    parser.add_argument('-r', '--reverse', action='store_true', help="Reverse the order of the listing")
    parser.add_argument('-t', '--time', action='store_true', help="Sort by time modified (oldest first)")

    args = parser.parse_args()
    
    # Load the directory structure
    directory_structure = load_directory_structure(args.file)
    
    # Determine which options to use
    items = list_directory_contents(
        directory_structure, 
        all_files=args.all, 
        almost_all=args.almost_all, 
        long_format=args.long, 
        reverse=args.reverse,
        sort_by_time=args.time
    )
    
    # Print the items
    print("\n".join(items))

if __name__ == "__main__":
    main()


# subtask 6

import json
import argparse
import time
import sys

def load_directory_structure(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def format_time(epoch_time):
    return time.strftime("%b %d %H:%M", time.localtime(epoch_time))

def list_directory_contents(directory, all_files=False, almost_all=False, long_format=False, reverse=False, sort_by_time=False, filter_by=None):
    contents = directory.get('contents', [])
    items = []

    for item in contents:
        if not almost_all and item['name'].startswith('.'):
            continue
        if filter_by and item['type'] != filter_by:
            continue
        if long_format:
            permissions = item['permissions']
            size = item['size']
            time_modified = format_time(item['time_modified'])
            name = item['name']
            items.append((item['time_modified'], f"{permissions} {size} {time_modified} {name}"))
        else:
            items.append((item['time_modified'], item['name']))
    
    if sort_by_time:
        items.sort(key=lambda x: x[0])
    
    if reverse:
        items.reverse()

    return [item[1] for item in items]

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="List directory contents.")
    parser.add_argument('file', type=str, help="Path to the JSON file describing the directory structure.")
    parser.add_argument('-a', '--all', action='store_true', help="Do not ignore entries starting with .")
    parser.add_argument('-A', '--almost-all', action='store_true', help="Include almost all entries, including .")
    parser.add_argument('-l', '--long', action='store_true', help="Use a long listing format")
    parser.add_argument('-r', '--reverse', action='store_true', help="Reverse the order of the listing")
    parser.add_argument('-t', '--time', action='store_true', help="Sort by time modified (oldest first)")
    parser.add_argument('--filter', type=str, choices=['file', 'dir'], help="Filter the listing by file or directory")

    args = parser.parse_args()
    
    # Load the directory structure
    directory_structure = load_directory_structure(args.file)
    
    # Determine which options to use
    items = list_directory_contents(
        directory_structure, 
        all_files=args.all, 
        almost_all=args.almost_all, 
        long_format=args.long, 
        reverse=args.reverse,
        sort_by_time=args.time,
        filter_by=args.filter
    )
    
    # Print the items
    print("\n".join(items))

if __name__ == "__main__":
    main()

# subtask 7

import json
import argparse
import time
import sys
import os

def load_directory_structure(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def format_time(epoch_time):
    return time.strftime("%b %d %H:%M", time.localtime(epoch_time))

def list_directory_contents(directory, all_files=False, almost_all=False, long_format=False, reverse=False, sort_by_time=False, filter_by=None):
    contents = directory.get('contents', [])
    items = []

    for item in contents:
        if not almost_all and item['name'].startswith('.'):
            continue
        if filter_by and item['type'] != filter_by:
            continue
        if long_format:
            permissions = item['permissions']
            size = item['size']
            time_modified = format_time(item['time_modified'])
            name = item['name']
            items.append((item['time_modified'], f"{permissions} {size} {time_modified} {name}"))
        else:
            items.append((item['time_modified'], item['name']))
    
    if sort_by_time:
        items.sort(key=lambda x: x[0])
    
    if reverse:
        items.reverse()

    return [item[1] for item in items]

def find_path(directory, path):
    components = path.strip("/").split("/")
    current = directory

    for component in components:
        found = False
        for item in current.get('contents', []):
            if item['name'] == component:
                if item['type'] == 'dir':
                    current = item
                elif item['type'] == 'file' and component == components[-1]:
                    return item
                found = True
                break
        if not found:
            return None

    return current

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="List directory contents.")
    parser.add_argument('path', nargs='?', default='.', help="Path within the directory structure.")
    parser.add_argument('file', type=str, help="Path to the JSON file describing the directory structure.")
    parser.add_argument('-a', '--all', action='store_true', help="Do not ignore entries starting with .")
    parser.add_argument('-A', '--almost-all', action='store_true', help="Include almost all entries, including .")
    parser.add_argument('-l', '--long', action='store_true', help="Use a long listing format")
    parser.add_argument('-r', '--reverse', action='store_true', help="Reverse the order of the listing")
    parser.add_argument('-t', '--time', action='store_true', help="Sort by time modified (oldest first)")
    parser.add_argument('--filter', type=str, choices=['file', 'dir'], help="Filter the listing by file or directory")

    args = parser.parse_args()
    
    # Load the directory structure
    directory_structure = load_directory_structure(args.file)
    
    # Find the specified path
    path_to_list = find_path(directory_structure, args.path)
    
    if path_to_list is None:
        print(f"error: cannot access '{args.path}': No such file or directory")
        sys.exit(1)
    
    if path_to_list['type'] == 'file':
        if args.long:
            permissions = path_to_list['permissions']
            size = path_to_list['size']
            time_modified = format_time(path_to_list['time_modified'])
            name = path_to_list['name']
            print(f"{permissions} {size} {time_modified} ./{args.path}")
        else:
            print(args.path)
    else:
        # Determine which options to use
        items = list_directory_contents(
            path_to_list, 
            all_files=args.all, 
            almost_all=args.almost_all, 
            long_format=args.long, 
            reverse=args.reverse,
            sort_by_time=args.time,
            filter_by=args.filter
        )
        
        # Print the items
        print("\n".join(items))

if __name__ == "__main__":
    main()


#subtask 8

import json
import argparse
import time
import sys

def load_directory_structure(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def format_time(epoch_time):
    return time.strftime("%b %d %H:%M", time.localtime(epoch_time))

def human_readable_size(size):
    for unit in ['B', 'K', 'M', 'G', 'T', 'P']:
        if size < 1024:
            return f"{size:.1f}{unit}" if unit != 'B' else f"{size}{unit}"
        size /= 1024

def list_directory_contents(directory, all_files=False, almost_all=False, long_format=False, reverse=False, sort_by_time=False, filter_by=None):
    contents = directory.get('contents', [])
    items = []

    for item in contents:
        if not almost_all and item['name'].startswith('.'):
            continue
        if filter_by and item['type'] != filter_by:
            continue
        if long_format:
            permissions = item['permissions']
            size = human_readable_size(item['size'])
            time_modified = format_time(item['time_modified'])
            name = item['name']
            items.append((item['time_modified'], f"{permissions} {size} {time_modified} {name}"))
        else:
            items.append((item['time_modified'], item['name']))
    
    if sort_by_time:
        items.sort(key=lambda x: x[0])
    
    if reverse:
        items.reverse()

    return [item[1] for item in items]

def find_path(directory, path):
    components = path.strip("/").split("/")
    current = directory

    for component in components:
        found = False
        for item in current.get('contents', []):
            if item['name'] == component:
                if item['type'] == 'dir':
                    current = item
                elif item['type'] == 'file' and component == components[-1]:
                    return item
                found = True
                break
        if not found:
            return None

    return current

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(description="List directory contents.")
    parser.add_argument('file', type=str, help="Path to the JSON file describing the directory structure.")
    parser.add_argument('path', nargs='?', default='.', help="Path within the directory structure.")
    parser.add_argument('-a', '--all', action='store_true', help="Do not ignore entries starting with .")
    parser.add_argument('-A', '--almost-all', action='store_true', help="Include almost all entries, including .")
    parser.add_argument('-l', '--long', action='store_true', help="Use a long listing format")
    parser.add_argument('-r', '--reverse', action='store_true', help="Reverse the order of the listing")
    parser.add_argument('-t', '--time', action='store_true', help="Sort by time modified (oldest first)")
    parser.add_argument('--filter', type=str, choices=['file', 'dir'], help="Filter the listing by file or directory")

    args = parser.parse_args()
    
    # Load the directory structure
    directory_structure = load_directory_structure(args.file)
    
    # Find the specified path
    path_to_list = find_path(directory_structure, args.path)
    
    if path_to_list is None:
        print(f"error: cannot access '{args.path}': No such file or directory")
        sys.exit(1)
    
    if path_to_list['type'] == 'file':
        if args.long:
            permissions = path_to_list['permissions']
            size = human_readable_size(path_to_list['size'])
            time_modified = format_time(path_to_list['time_modified'])
            name = path_to_list['name']
            print(f"{permissions} {size} {time_modified} ./{args.path}")
        else:
            print(args.path)
    else:
        # Determine which options to use
        items = list_directory_contents(
            path_to_list, 
            all_files=args.all, 
            almost_all=args.almost_all, 
            long_format=args.long, 
            reverse=args.reverse,
            sort_by_time=args.time,
            filter_by=args.filter
        )
        
        # Print the items
        print("\n".join(items))

if __name__ == "__main__":
    main()

#subtask 9

import json
import argparse
import time
import sys

def load_directory_structure(file_path):
    with open(file_path, 'r') as file:
        return json.load(file)

def format_time(epoch_time):
    return time.strftime("%b %d %H:%M", time.localtime(epoch_time))

def human_readable_size(size):
    for unit in ['B', 'K', 'M', 'G', 'T', 'P']:
        if size < 1024:
            return f"{size:.1f}{unit}" if unit != 'B' else f"{size}{unit}"
        size /= 1024

def list_directory_contents(directory, all_files=False, almost_all=False, long_format=False, reverse=False, sort_by_time=False, filter_by=None):
    contents = directory.get('contents', [])
    items = []

    for item in contents:
        if not almost_all and item['name'].startswith('.'):
            continue
        if filter_by and item['type'] != filter_by:
            continue
        if long_format:
            permissions = item['permissions']
            size = human_readable_size(item['size'])
            time_modified = format_time(item['time_modified'])
            name = item['name']
            items.append((item['time_modified'], f"{permissions} {size} {time_modified} {name}"))
        else:
            items.append((item['time_modified'], item['name']))
    
    if sort_by_time:
        items.sort(key=lambda x: x[0])
    
    if reverse:
        items.reverse()

    return [item[1] for item in items]

def find_path(directory, path):
    components = path.strip("/").split("/")
    current = directory

    for component in components:
        found = False
        for item in current.get('contents', []):
            if item['name'] == component:
                if item['type'] == 'dir':
                    current = item
                elif item['type'] == 'file' and component == components[-1]:
                    return item
                found = True
                break
        if not found:
            return None

    return current

def main():
    # Parse command-line arguments
    parser = argparse.ArgumentParser(
        description="pyls - A Python script to list directory contents in a style similar to 'ls'.",
        epilog="Examples:\n" 
               "  python -m pyls -l parser\n" 
               "  python -m pyls -l -r -t --filter=dir\n"
               "  python -m pyls non_existent_path\n",
        formatter_class=argparse.RawTextHelpFormatter
    )
    parser.add_argument('file', type=str, help="Path to the JSON file describing the directory structure.")
    parser.add_argument('path', nargs='?', default='.', help="Path within the directory structure (default is the current directory).")
    parser.add_argument('-a', '--all', action='store_true', help="Do not ignore entries starting with '.'")
    parser.add_argument('-A', '--almost-all', action='store_true', help="Include almost all entries, including '.'")
    parser.add_argument('-l', '--long', action='store_true', help="Use a long listing format")
    parser.add_argument('-r', '--reverse', action='store_true', help="Reverse the order of the listing")
    parser.add_argument('-t', '--time', action='store_true', help="Sort by time modified (oldest first)")
    parser.add_argument('--filter', type=str, choices=['file', 'dir'], help="Filter the listing by file or directory")

    args = parser.parse_args()
    
    # Load the directory structure
    directory_structure = load_directory_structure(args.file)
    
    # Find the specified path
    path_to_list = find_path(directory_structure, args.path)
    
    if path_to_list is None:
        print(f"error: cannot access '{args.path}': No such file or directory")
        sys.exit(1)
    
    if path_to_list['type'] == 'file':
        if args.long:
            permissions = path_to_list['permissions']
            size = human_readable_size(path_to_list['size'])
            time_modified = format_time(path_to_list['time_modified'])
            name = path_to_list['name']
            print(f"{permissions} {size} {time_modified} ./{args.path}")
        else:
            print(args.path)
    else:
        # Determine which options to use
        items = list_directory_contents(
            path_to_list, 
            all_files=args.all, 
            almost_all=args.almost_all, 
            long_format=args.long, 
            reverse=args.reverse,
            sort_by_time=args.time,
            filter_by=args.filter
        )
        
        # Print the items
        print("\n".join(items))

if __name__ == "__main__":
    main()

    


