import sys

file1 = sys.argv[1]
file2 = sys.argv[2]

with open(file1) as f1:
    content_file1 = f1.readlines()
with open (file2) as f2:
    content_file2 = f2.readlines()

with open(file1, "w") as f1:
    f1.writelines(content_file2)
with open (file2,"w") as f2:
    f2.readlines(content_file1)
