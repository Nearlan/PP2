import os

if os.path.exists("Docs\MydogInfo.txt"):
    print(os.path.basename("Docs\MydogInfo.txt"))
    print(os.path.dirname("Docs\MydogInfo.txt"))
else:
    print("Nothing there")