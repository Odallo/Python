import os, shutil

def organize(folder):
    for filename in os.listdir(folder):
        filepath = os.path.join(folder, filename)
        if os.path.isfile(filepath):
            ext = filename.split(".")[-1]
            dest_folder = os.path.join(folder, ext)
            os.makedirs(dest_folder, exist_ok=True)
            shutil.move(filepath, os.path.join(dest_folder, filename))

organize("/home/odallo/Downloads")  # change path
