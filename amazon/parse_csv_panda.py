import pandas as pd
import re

reg_dict = {
    'school': re.compile(r'School = (?P<school>.*)\n'),
    'grade': re.compile(r'Grade = (?P<grade>.*)\n'),
    'name_score': re.compile(r'(?P<name_score>Name|Score)')
}

