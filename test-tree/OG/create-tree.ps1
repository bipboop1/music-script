# Define folder names
$folders = "A", "B", "C"
$subfolders = "1", "2", "3"
$fileNames = "a", "b", "c"

# Create main folders A, B, C
foreach ($folder in $folders) {
	New-Item -ItemType Directory -Path $folder
	foreach ($subfolder in $subfolders) {
		$subfolderName = "$folder$subfolder"
		New-Item -ItemType Directory -Path $folder\$subfolderName
		foreach ($fileName in $fileNames) {
			$mp3FileName = "$subfolderName$fileName.mp3"
			New-Item -ItemType File -Path $folder\$subfolderName -Name $mp3FileName
		}
	}
}
