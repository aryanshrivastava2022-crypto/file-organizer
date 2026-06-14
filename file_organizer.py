import os
import shutil

path = input("Enter folder path to organize: ")

files = os.listdir(path)

for file in files:
    file_path = os.path.join(path, file)

    if os.path.isfile(file_path):
        extension = file.split(".")[-1].lower()

        folder_name = extension.upper() + "_Files"
        folder_path = os.path.join(path, folder_name)

        if not os.path.exists(folder_path):
            os.makedirs(folder_path)

        shutil.move(file_path, os.path.join(folder_path, file))

print("✅ Files organized successfully!")
