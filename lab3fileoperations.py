import os
import sys

def count_search_text_in_file(file_path, search_text):
    try:
        with open(file_path, 'r', encoding='utf-8') as file:
            content = file.read()
            return content.lower().count(search_text.lower())
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return 0

def search_text_in_files(directory, search_text):
    for root, dirs, files in os.walk(directory):
        for file in files:
            file_path = os.path.join(root, file)
            count = count_search_text_in_file(file_path, search_text)
            if count > 0:
                print(f"File: {file_path} | '{search_text}' found {count} times.")


if len(sys.argv) != 3:
    print("Usage: python script.py <directory_path> <search_text>")
    sys.exit(1)

directory = sys.argv[1]
search_text = sys.argv[2]

print(f"\nSearching for '{search_text}' in all files within '{directory}'...\n")
search_text_in_files(directory, search_text)


# python script.py /path/to/directory "search term"