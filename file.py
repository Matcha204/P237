import os
import shutil

source = "file1.txt"
dest = "file2.txt"

os.rename(source, dest)
print("File renamed")