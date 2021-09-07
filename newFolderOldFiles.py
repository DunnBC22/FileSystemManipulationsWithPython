import os
from posix import listdir
import re
from tkinter.filedialog import *
from tkinter.simpledialog import *


def define_subfolder_name():
    subfolder_name = askstring(
        title="Subfolder Name", prompt="What would you like to name the subfolder?", initialvalue="default")
    if (subfolder_name is None or subfolder_name == ''):
        return define_subfolder_name()
    else:
        return subfolder_name


def move_doc_files():
    folder_name = askdirectory(
        title="What directory/folder to move doc files to a new subdirectory")
    os.chdir(folder_name)

    new_subfolder_name_input = define_subfolder_name()
    print(new_subfolder_name_input)

    new_subfolder_name = re.sub(
        '([^A-Za-z0-9 ])', '', new_subfolder_name_input)

    new_folder = os.path.join(folder_name + '/' + new_subfolder_name)
    mkdir_new_folder = r'mkdir -v ' + new_folder

    os.system(mkdir_new_folder)
    os.chdir(new_folder)

    # Build the move command then run that command
    move_command = r'mv ' + folder_name + '/* ' + new_folder
    os.system(move_command)


if __name__ == '__main__':
    move_doc_files()
    quit()
