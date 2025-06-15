import os
files = glob.glob("*.txt")
files.sort(key=os.path.gettime)
print("\n".join(files))
