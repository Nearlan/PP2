import os
print("Directories", [name for name in os.listdir("MyPc") if os.path.isdir(os.path.join("MyPc", name))])
print("Files", [name for name in os.listdir("MyPc") if os.path.isfile(os.path.join("MyPc", name))])
print("Everything", os.listdir("MyPc"))