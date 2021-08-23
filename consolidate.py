# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""
import shutil



from pathlib import Path
from pprint import pprint

p = Path('C:\\Users\\zine5\\OneDrive\\Documentos\\Soulseek Downloads\\complete')

# All subdirectories in the current directory, not recursive.
dirs = [f for f in p.iterdir() if f.is_dir()]

for dir in dirs:
    print(dir)
    dirr = Path(dir)
    files = [f for f in dirr.iterdir()]
    for file in files:
        original =  str(file) 
        target = r'C:\\Users\\zine5\\OneDrive\\Documentos\\Soulseek Downloads\\consolidated'
        shutil.move(original,target)

    #print(files)


#pprint(dirs)
