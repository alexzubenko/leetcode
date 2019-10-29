"""
how to work with os object like files and directories
"""

import os
# how to use datetime to parse unix timestamp
from datetime import datetime

# os.chdir("C:\\Users\\Oleksandr_Zubenko\\PycharmProjects\\leetcode")
print(os.getcwd())
for file in os.listdir():
    print(file)
print(os.listdir())

# Create the directory
# os.mkdir - create directory
# os.makedirs - create directories if we need to create directories tree,
# this method will create all the directories along the way if needed

try:
    os.mkdir('tests')
    os.makedirs('test/subtest')
except:
    print('directories already there')

# Remove directories
# os.rmdir - remove one directory
# os.removedirs - remove directories tree

os.rmdir('tests')
os.removedirs('test/subtest')

# renaming files
# os.rename(file, new_name)
try:
    os.rename('file.txt', 'file.jpg')
except:
    pass
os.rename('file.jpg', 'file.txt')

# how to get info about file
# os.stat(file_name)

print(os.stat('file.txt'))

# how to get the particular atribute from the stat
mod_time = os.stat('file.txt').st_mtime
print(mod_time)

# how to transfer this to the readble time
print(datetime.fromtimestamp(mod_time))

