import os 

CHANGED_FILES = os.environ.get("CHANGED_FILES")
CURRENT_USER = os.environ.get("CURRENT_USER")


print("Inside validateUser.py")
print(CHANGED_FILES)
print(CURRENT_USER)
