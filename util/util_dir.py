import os
import glob2   #pip install glob2

def help_dir():
    print(dir(os))
    print(dir(str))
    help (os)
    
def list_files_patterns():
    
    print(glob2.glob("*.txt"))
    
list_files_patterns()