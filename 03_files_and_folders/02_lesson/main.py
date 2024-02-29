from pathlib import Path

root_dir = Path("files")
print(root_dir)
file_paths = root_dir.iterdir()

for path in file_paths:
    new_filename = "new-" + path.stem + path.suffix
    print(new_filename)
    new_filepath = path.with_name(new_filename)
    print(new_filepath)
    path.rename(new_filepath)
