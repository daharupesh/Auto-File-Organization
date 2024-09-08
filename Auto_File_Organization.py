import os, shutil
import pandas as pd

file_types = pd.read_json('test.json')

def get_path():
    '''
    Get the folder path from the user.
    This function prompts the user to enter a folder path, checks if the path exists, and returns the path if valid.

    Returns:
        path (str): The valid folder path entered by the user.
    '''

    path = input("Enter path (e.g., C:\\Users\\): ")

    if not os.path.exists(path): raise ValueError("Path does not exist.")
    
    return path

def organize_files(folder_path):
    '''
    Organize files into their corresponding folders based on extensions.
    This function reads the files from the provided folder path, checks their extensions, and moves them into categorized folders.

    Args:
        folder_path (str): The path of the folder containing files to be organized.

    Returns:
        None
    '''
    try:
        count_move = 0
        list_of_files = os.listdir(folder_path)  # List all files in the given folder
        
        for file in list_of_files:
            extension = file.split('.')[-1].lower()  # Get the file extension
            
            for category, data in file_types.items():
                if extension in data['Extensions']:
                    index = data['Extensions'].index(extension)
                    file_name = data['File Names'][index]

                    category_path = os.path.join(folder_path, category)
                    specific_path = os.path.join(category_path, file_name)

                    if not os.path.exists(specific_path):
                        os.makedirs(specific_path)  # Create the folder if it doesn't exist

                    source = os.path.join(folder_path, file)
                    destination = os.path.join(specific_path, file)
                    
                    shutil.move(source, destination)  # Move the file to the new location
                    print(f"'{file}' moved to '{file_name}'")
                    count_move += 1
                    break
        
        print(f"Total files moved: {count_move}")
    except Exception as e:
        print(f"Error: {e}")

def main():
    """
     The main function that initiates the file organization process.
      workflow:-
      - Retrieves a folder path from the user by calling the `get_path()` function.
      - Calls the `organize_files(folder_path)` function to organize the files in the specified folder.
      - Prints a success message once the files are organized successfully otherwise error message.
      
    """
    try:
        folder_path = get_path()  # Get the folder path from the user
        organize_files(folder_path)
        print("File Organize successfully")
    except Exception as e:
        print(e)

if __name__ == "__main__":
    main()
  