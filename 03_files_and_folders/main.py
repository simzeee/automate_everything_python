from pathlib import Path

p1 = Path(
    "/Users/johnsims/Desktop/automate_everything_python/03_files_and_folders/txt_files/abc.txt"
)

with open(p1, "r") as file:
    print(file.read())


print(p1.name)
print(p1.stem)
print(p1.suffix)

p2 = Path("txt_files")
print(p2.iterdir())
for item in p2.iterdir():
    print(item)

print(list(p2.iterdir()))