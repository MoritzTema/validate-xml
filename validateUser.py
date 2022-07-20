import os 

CHANGED_FILES = os.environ.get("CHANGED_FILES")
CURRENT_USER = os.environ.get("CURRENT_USER")
ALLOWED_USERS = os.environ.get("ALLOWED_USERS")


print("Inside validateUser.py")
print(CHANGED_FILES)
print(CURRENT_USER)
print(ALLOWED_USERS)
