import os
import sys

print("Running 2 scripts main UI and recvflag")
os.system("python index.py & python recvflag.py &") 
print("Done")
