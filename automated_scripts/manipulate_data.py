import json
import re
import pickle
from datetime import datetime

username = "charleskristopher"

# Get the current date
current_date = datetime.now().strftime("%Y%m%d")

GLOBAL_CONTACTS_PATH = "path\\to\\OfflineGALContacts.txt"
GLOBAL_CONTACTS_INDEX_SAVE_PATH = f"path\\to\\GlobalContactsIndex.pkl"
GLOBAL_CONTACTS_ARCHIVE_PATH = f"path\\to\\archive\\GlobalContactsIndex_{current_date}.pkl"

# Where the scraped data is stored
PUBLIC_FOLDERS_PATH = "path\\to\\PublicFoldersIndex.txt"
# Where the indexed data needs to be saved at
PUBLIC_FOLDERS_INDEX_SAVE_PATH = f"path\\to\\PublicFolderIndex.pkl"
PUBLIC_FOLDERS_INDEX_ARCHIVE_PATH = f"path\\to\\archive\\PublicFolderIndex_{current_date}.pkl"


def remove_my_email():
    # Assuming self.username is defined somewhere in your code
    # username = "charleskristopher"

    # Path to your pickle file
    pickle_file_path = f"path\\to\\PublicFolderIndex.pkl"

    
    # Function to modify paths in a list
    def modify_paths(paths_list):
        prefix_to_remove = "\\\\Public Folders - redacted@uams.edu"
        modified_paths = []
        
        for path in paths_list:
            modified_path = path.replace(prefix_to_remove, "").strip("\\")
            modified_paths.append(modified_path)
        
        return modified_paths

    # Load the pickle file
    with open(pickle_file_path, 'rb') as f:
        data = pickle.load(f)

    # Modify values (assuming each value is a list of paths)
    modified_data = {key: modify_paths(value) for key, value in data.items()}

    # Print first and last 10 modified paths for verification
    print("First 10 modified paths:")
    for idx, (key, paths) in enumerate(list(modified_data.items())[:10]):
        print(f"{idx+1}. {key}: {paths}")

    print("\nLast 10 modified paths:")
    for idx, (key, paths) in enumerate(list(modified_data.items())[-10:]):
        print(f"{len(modified_data) - 9 + idx}. {key}: {paths}")


def create_index_for_global(paths_file):
    index = {}
    
    try:
        with open(paths_file, 'r', encoding='utf-8', errors='replace') as file:
            lines = file.readlines()
            
            i = 0
            while i < len(lines):
                if lines[i].startswith("Name:"):
                    skip = False
                    
                    # Extract Name and Email
                    try:
                        name = lines[i].strip().split(": ", 1)[1]
                    except IndexError as e:
                        print(f"SKIPPING THIS CONTACT")
                        print(f"lines[i]: {lines[i]}")
                        print(f"lines[i]: {lines[i+1]}")
                        print(f"lines[i]: {lines[i+2]}")
                        skip = True
                    try:
                        email = lines[i+1].strip().split(": ", 1)[1]
                    except IndexError as e:
                        print(f"SKIPPING THIS CONTACT")
                        print(f"lines[i]: {lines[i]}")
                        print(f"lines[i]: {lines[i+1]}")
                        print(f"lines[i]: {lines[i+2]}")
                        skip = True
                    
                    # if email
                    # Store in index
                    if not skip:                        
                        index[name] = f"{name}: {email}"
                        index[email] = f"{name}: {email}"
                    else:
                        print(f"Skip - Name: {name}; Email: {email}")
                    
                    # Move to the next block (assuming each contact block is separated by '----------------------------------------')
                    
                    i += 3  # move i to skip the next two lines and the separator line
                    
                else:
                    i += 1  # move i to next line if no valid name line found
                
    except FileNotFoundError:
        print(f"Error: File '{paths_file}' not found.")
    
    return index



def main():
    pass


def create_index_from_paths(_path):
    path_index = {}

    with open(_path, 'r', encoding='utf-8', errors='replace') as file:
        for line in file:
            _path = line.strip()

            dir_name = _path.split('\\')[-1]

            if dir_name in path_index:
                path_index[dir_name].append(_path)
            else:
                path_index[dir_name] = [_path]
    return path_index


def search_paths(idx, directory_name):
    # Search for the directory name in the index and return the corresponding paths
    return idx.get(directory_name, [])


def save_index(idx, file_path):
    with open(file_path, 'wb') as file:
        pickle.dump(idx, file)


def load_index(file_path):
    with open(file_path, 'rb') as file:
        idx = pickle.load(file)
    return idx


def clean_and_save_global_contact_data():
    """
    Official method to clean and save the Global Contacts Data
    """
    g_index = create_index_for_global(GLOBAL_CONTACTS_PATH)
    save_index(g_index, GLOBAL_CONTACTS_INDEX_SAVE_PATH)
    save_index(g_index, GLOBAL_CONTACTS_ARCHIVE_PATH)


def clean_and_save_public_folders():
    """
    Official method to clean and save the Public Folders Data
    """
    index = create_index_from_paths(PUBLIC_FOLDERS_PATH)
    save_index(index, PUBLIC_FOLDERS_INDEX_SAVE_PATH)
    save_index(index, PUBLIC_FOLDERS_INDEX_ARCHIVE_PATH)


if __name__ == '__main__':
    # SETUP TO TAKE COMMAND LINE ARGS
    # USE AN ARG TO PASS A STRING THAT WILL DETERMINE 'PUBLIC' OR 'GLOBAL' TO INDICATE THE DATA THAT IS TO BE CLEANED
    # OR JUST RUN THEM AT THE SAME TIME EACH WEEK AFTER EACH OF THEM HAVE BEEN SCRAPED.
    clean_and_save_global_contact_data()
    clean_and_save_public_folders()
