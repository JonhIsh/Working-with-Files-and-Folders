from pathlib import Path
import zipfile

root_dir = Path('files')
archive_path = root_dir / Path("archive.zip")

with zipfile.ZipFile(archive_path, 'w') as archive:
  file_paths = root_dir.rglob("*.txt")
  
  for path in file_paths:
    if path.is_file():
      archive.write(path)