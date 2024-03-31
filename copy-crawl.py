import os
import random
import shutil
import time
import colorama
from colorama import Fore, Back, Style
from pathlib import Path

def count_base_subdirs(src_dir):
	# Count the number of direct subdirectories in src_dir
	return sum(1 for _ in os.scandir(src_dir) if _.is_dir())

def copy_random_file(src_dir, dest_dir):
	total_subdirs = count_base_subdirs(src_dir)
	print(f"{Fore.CYAN}Total number of artists: {Fore.YELLOW}{total_subdirs}{Style.RESET_ALL}")
	current_subdir = 0

	for subdir, dirs, files in os.walk(src_dir):
		# only count and update for base subdirectories
		if Path(subdir).parent == Path(src_dir):
			current_subdir += 1
			print(f"{Fore.CYAN}crawling through artist {Fore.YELLOW}[{current_subdir}/{total_subdirs}]{Fore.CYAN}...{Style.RESET_ALL}")

		mp3_files = [file for file in files if file.endswith('.mp3')]
		if mp3_files:
			selected_file = random.choice(mp3_files)
			src_file_path = os.path.join(subdir, selected_file)
			
			# Calculate relative path to maintain folder structure
			relative_path = os.path.relpath(subdir, src_dir)
			dest_subdir = os.path.join(dest_dir, relative_path)
			
			# Ensure destination subdir exists
			os.makedirs(dest_subdir, exist_ok=True)
			
			dest_file_path = os.path.join(dest_subdir, selected_file)
			shutil.copy2(src_file_path, dest_file_path)
			print(f"copied {src_file_path} to {dest_file_path}")
			time.sleep(1)

# Replace these paths with your actual paths
source_directory = ".\\test-tree\\OG"
destination_directory = ".\\test-tree\\dest"

# Ensure the destination directory exists
Path(destination_directory).mkdir(parents=True, exist_ok=True)

copy_random_file(source_directory, destination_directory)
