import os
import re

folder_path = "./your/path/to/folder"

for filename in os.listdir(folder_path):
    if os.path.isfile(os.path.join(folder_path, filename)):
        match = re.search(r"\((.*?)\)", filename)
        if match:
            author_date = match.group(1)
            author_date = re.sub(r"(\w+) y (\w+)", r"\1 & \2", author_date)
            new_filename = re.sub(r"\((.*?)\)", author_date, filename)
            os.rename(os.path.join(folder_path, filename), os.path.join(folder_path, new_filename))
            print(f"Renamed {filename} to {new_filename}")



# This script uses the os and re modules to loop through all files in the specified folder and rename any files that match the pattern of starting with an author and date enclosed in parentheses. 
# The regular expression r"\((.*?)\)" matches anything enclosed in parentheses 
# The re.sub() method replaces it with an empty string, effectively removing the parentheses.
# Using match.group(1) to keep format "Author et al, YYYY". Then, it uses that information to construct the new filename with the same format.