from platform import machine
from os import system
m=machine()
if "aarch" in m:
 system("chmod 777 aarch && ./aarch")
else:
 system("chmod 777 arm && ./arm")
