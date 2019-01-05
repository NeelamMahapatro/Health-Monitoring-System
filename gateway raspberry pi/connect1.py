#!usr/bin/python
#!usr/bin/wvdial
#!usr/bin/wvdialconf

import os
import time

print("Before sleep")
time.sleep(25)
os.system("/usr/bin/wvdial 3gconnect")
print("After")
