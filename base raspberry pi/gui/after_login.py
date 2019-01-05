import os
import sys

print("Running 2 scripts simultaneously")
os.system("python icon.py & python servertosend.py &") 
print("Done")
