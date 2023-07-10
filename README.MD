# Renaming files inside a folder

As a student or scientist, I found myself downloading too many papers and having a specific naming convention for them. After some time, I decided including parenthesis in the names was not useful and instead of going through renaming each file individually, I created two simple python scripts. Both loop through file names in a folder and rename them. If you have a naming convention or have parts of the file name you want to modify, then manipulating the regular expression in the script will help you to rename them as wanted.


## How to run this script  
The script ``rename.py`` loops through the filenames inside a specified folder and renames them. However, changes are definite and cannot be undone. As that may be too compromising if you haven't tested the regular expression you want to use, then ``rename_to_folder.py`` will be useful. This script loops through the filenames but instead of overwriting the names, it created a new folder with the renamed files. 

Sample files are included inside the *sample_files* folder to test both scripts. After running ``rename_to_folder.py``, a new folder called *renamed_files* will be created within the directory, storing the newly renamed files. 