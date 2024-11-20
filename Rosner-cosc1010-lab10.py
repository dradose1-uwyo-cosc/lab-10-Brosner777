# Braxton Rosner
# UWYO COSC 1010
# Submission Date 11/20/24
# Lab 10
# Lab Section: 15
# Sources, people worked with, help given to: Stackoverflow form on using hash files in the code. Python Crash Course on accessing files
# 
# comments
# here

#import modules you will need 

from hashlib import sha256 
from pathlib import Path

def get_hash(to_hash):
    """You can use """
    return sha256(to_hash.encode('utf-8')).hexdigest().upper()
def read_file(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as file:
            return file.readlines()
    except:
        return None 

def crack_password(hash_file, password_file):
    hash_lines = read_file(hash_file)
    if not hash_lines:
        return
    
    stored_hash = hash_lines[0].strip() 

    passwords = read_file(password_file)
    if not passwords:
        return 

    for password in passwords:
        password = password.strip()
        if get_hash(password) == stored_hash:
            print(f"The password is: {password}")
            return
    print("No matching password found.")

hash_text = "hash"
rockyou_text = "rockyou.txt"

crack_password(hash_text, rockyou_text)

