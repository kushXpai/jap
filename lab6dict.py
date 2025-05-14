from collections import defaultdict

def groupAndSortOwners(file_dict):
    grouped = defaultdict(list)
    
    # Group files by owner
    for file, owner in file_dict.items():
        grouped[owner].append(file)
    
    # Sort the file list for each owner
    for owner in grouped:
        grouped[owner].sort()
    
    return dict(grouped)

files = {
    'Input.txt': 'Albert',
    'Code.py': 'Stan',
    'Output.txt': 'Albert',
    'btech.txt': 'Albert'
}

result = groupAndSortOwners(files)
print(result)