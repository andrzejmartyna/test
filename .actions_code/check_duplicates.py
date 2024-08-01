# initial version generated using phind.com

import os

def find_duplicates(directory):
    """
    Recursively searches through files in the given directory,
    checking for duplicate lines within each file.
    """
    duplicates_found = False
    
    print(f"Checking: '{directory}' ...")
    
    for root, dirs, files in os.walk(directory):
        for file in files:
            if not file.endswith(".txt"):
                print(f"Skipped: '{file}'")
                continue

            filepath = os.path.join(root, file)
            try:
                with open(filepath, 'r', encoding='utf-8') as f:
                    lines = f.readlines()
                    seen_lines = set()
                    
                    for line in lines:
                        # Normalize line endings to avoid false positives due to OS differences
                        normalized_line = line.rstrip('\n')
                        
                        if normalized_line in seen_lines:
                            print(f"Duplicate found in {filepath}: '{normalized_line}'")
                            duplicates_found = True
                        else:
                            seen_lines.add(normalized_line)
            except Exception as e:
                print(f"Error processing {filepath}: {e}")
    
    return duplicates_found

if __name__ == "__main__":
    current_directory = os.getcwd()  # Assuming the script runs at the repo root
    duplicates_exist = find_duplicates(current_directory)
    
    if duplicates_exist:
        print("Duplicate lines were found.")
        exit(1)  # Exit with error code if duplicates were found
    else:
        print("No duplicate lines detected.")
        exit(0)  # Exit successfully if no duplicates were found
