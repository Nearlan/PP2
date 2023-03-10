import os

print("Exists", os.access("Docs\MydogInfo.txt", os.F_OK))
print("readability",os.access("MydogInfo.txt", os.R_OK))
print("writability",os.access("MydogInfo.txt", os.W_OK))
print(" executability",os.access("MydogInfo.txt", os.X_OK))