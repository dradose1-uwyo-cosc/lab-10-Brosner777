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
try:
    with open('hash', 'r') as file:
        hash_value = file.read().strip()
except Exception as e:
    print('Error:', e)
    
try:
    with open('rockyou.txt', 'r') as file:
        password_list = file.readlines()
except Exception as e:
    print('Error:', e)

for password in password_list:
    password = password.strip()
    if get_hash(password) == hash_value:
        print('Password:', password)
        break
