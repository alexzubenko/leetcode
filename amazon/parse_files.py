"""
print(sol.parser_memory_save("C:\Brother\syslog.txt"))


"""

import re
import os

def parse_file(path):
    if not os.path.isfile(path):
        print("no such file")
        return
    with open(path) as file:
        for line in file:
            if re.match(r'systemd', line.split()[4]):
                print(line)

parse_file("C:\Brother\syslog.txt")