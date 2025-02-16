from pathlib import Path

path = Path("abc.txt")

if path.exists():
    with open(path, "r") as file:
        print(file.read())
else:
    with open(path, "w") as file:
        file.write("Hello, World!")