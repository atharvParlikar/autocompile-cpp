import hashlib
import os
import time

starttime = time.time()
filepath = "" # enter the full filepath here...
compilecpp = "" # enter your compile command here... normally it will be something like g++ filename.cpp or filename.c

with open(filepath, 'rb') as f:
    fileHash = hashlib.md5(f.read()).hexdigest()    

print("Watching..\n")

while True:
    time.sleep(1.0)
    with open(filepath, 'rb') as f:
        currentHash = hashlib.md5(f.read()).hexdigest()
        if fileHash != currentHash:
            fileHash = currentHash
            if os.system(compilecpp) != 0:
                print("program compiled with errors")
            else: print("program compiled successfully")
