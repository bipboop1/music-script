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
	print(f"\n")
	print(f"{Fore.CYAN}▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀ ")
	print(f"{Fore.CYAN}total number of artists: {Fore.YELLOW}{total_subdirs}{Style.RESET_ALL}")
	current_subdir = 0
	song_count = 0
	total_song_count = 0

	for subdir, dirs, files in os.walk(src_dir):
		# only count and update for base subdirectories
		if Path(subdir).parent == Path(src_dir):
			current_subdir += 1
			artist_name = Path(subdir).name
			if song_count > 0:
				print(f"{Fore.CYAN}copied {Fore.GREEN}{song_count} {Fore.CYAN}songs{Style.RESET_ALL}")
			print(f"{Fore.CYAN}crawling through artist {Fore.RED}{artist_name} {Fore.YELLOW}[{current_subdir}/{total_subdirs}]{Fore.CYAN}...{Style.RESET_ALL}")
			song_count = 0

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
			print(f"{Fore.GREEN}copied {Style.RESET_ALL}{src_file_path} {Fore.GREEN}to {Style.RESET_ALL}{dest_file_path}")
			song_count += 1
			total_song_count += 1
			# time.sleep(1)
	print(f"{Fore.CYAN}copied {Fore.GREEN}{song_count} {Fore.CYAN}songs{Style.RESET_ALL}")
	print(f"\n")
	print(f"{Fore.CYAN}▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀▄▀ ")
	print(f"{Fore.CYAN}▀▄▀▄▀▄ done! {Fore.RED}WAlkmAn{Fore.CYAN} is ready. ▄▀▄▀▄▀ ")
	print(f"{Fore.CYAN}▀▄▀ copied {Fore.YELLOW}{total_song_count} {Fore.CYAN}songs from {Fore.YELLOW}{total_subdirs}{Fore.CYAN} artists.▀▄▀{Style.RESET_ALL}")
	print(f"\n")

# Replace these paths with your actual paths
# source_directory = "E:\Musique"
# destination_directory = "E:\WAlkmAn"
source_directory = ".\\test-tree\\OG"
destination_directory = ".\\test-tree\\dest"

# Ensure the destination directory exists
Path(destination_directory).mkdir(parents=True, exist_ok=True)

copy_random_file(source_directory, destination_directory)
