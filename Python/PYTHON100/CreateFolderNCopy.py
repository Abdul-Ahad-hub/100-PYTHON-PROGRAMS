from pathlib import Path
import shutil
def make_folder():
    new_folder = Path("new_folder")
    new_folder.mkdir(exist_ok=True)

def copy_file():
    shutil.copy("EvenOdd.py", "new_folder/copy.txt")

make_folder()
copy_file()

