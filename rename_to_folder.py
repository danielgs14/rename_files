import os
import re
import shutil

folder_path = "./sample_files"
new_folder_path = "./renamed_files"

# Create the new folder if it doesn't exist
if not os.path.exists(new_folder_path):
    os.makedirs(new_folder_path)

for filename in os.listdir(folder_path):
    if os.path.isfile(os.path.join(folder_path, filename)):
        match = re.search(r"\((.*?)\)", filename)
        if match:
            author_date = match.group(1)
            author_date = re.sub(r"(\w+) y (\w+)", r"\1 & \2", author_date)
            new_filename = re.sub(r"\((.*?)\)", author_date, filename)
            
            old_file_path = os.path.join(folder_path, filename)
            new_file_path = os.path.join(new_folder_path, new_filename)
            
            shutil.copy2(old_file_path, new_file_path)
            print(f"Copied {filename} to {new_file_path}")

# This script uses the os and re modules to loop through all files in the specified folder and rename any files that match the pattern of starting with an author and date enclosed in parentheses. The shutil module will copy the files and store them in the new folder.
# The regular expression r"\((.*?)\)" matches anything enclosed in parentheses 
# The re.sub() method replaces it with an empty string, effectively removing the parentheses.
# Using match.group(1) to keep format "Author et al, YYYY". Then, it uses that information to construct the new filename with the same format.