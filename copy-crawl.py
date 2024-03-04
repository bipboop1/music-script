import os
import random
import shutil
from pathlib import Path

def copy_random_file(src_dir, dest_dir):
    for subdir, dirs, files in os.walk(src_dir):
        if files:
            selected_file = random.choice(files)
            src_file_path = os.path.join(subdir, selected_file)
            
            # Calculate relative path to maintain folder structure
            relative_path = os.path.relpath(subdir, src_dir)
            dest_subdir = os.path.join(dest_dir, relative_path)
            
            # Ensure destination subdir exists
            os.makedirs(dest_subdir, exist_ok=True)
            
            dest_file_path = os.path.join(dest_subdir, selected_file)
            shutil.copy2(src_file_path, dest_file_path)
            print(f"Copied {src_file_path} to {dest_file_path}")

# Replace these paths with your actual paths
source_directory = "C:\\Users\\Shamsi\\Documents\\code\\music-script\\test-tree\\OG"
destination_directory = "C:\\Users\\Shamsi\\Documents\\code\\music-script\\test-tree\\dest"

# Ensure the destination directory exists
Path(destination_directory).mkdir(parents=True, exist_ok=True)

copy_random_file(source_directory, destination_directory)
