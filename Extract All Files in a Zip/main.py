from pathlib import Path
import zipfile

root_dir = Path('files')
archive_path = root_dir / Path("archive.zip")

for path in root_dir.glob("*.zip"):
  with zipfile.ZipFile(path, 'r') as zip_file:
    zip_file.extractall(root_dir)