"""
https://leetcode.com/discuss/interview-question/391865/Facebook-Software-Engineer-Phone-Screen-Interview-Questions-or-REJECT/352301

You will be supplied with two data files in CSV format .
The first file contains statistics about various dinosaurs. The second file contains additional data.
Given the following formula, speed = ((STRIDE_LENGTH / LEG_LENGTH) - 1) * SQRT(LEG_LENGTH * g)
Where g = 9.8 m/s^2 (gravitational constant)

Write a program to read in the data files from disk, it must then print the names of only the bipedal dinosaurs from fastest to slowest.
Do not print any other information.

"""

import math

def find_bipedal_speed(file1, file2):
    g = 9.8
    bipedal_dinos = {}
    result = {}
    with open(file2) as f:
        for line in f:
            NAME, STRIDE_LENGTH, STANCE = line.strip().split(',')
            if STANCE == "bipedal":
                bipedal_dinos[NAME] = float(STRIDE_LENGTH)

    with open(file1) as f:
        for line in f:
            NAME, LEG_LENGTH, DIET = line.strip().split(',')
            if NAME in bipedal_dinos:
                STRIDE_LENGTH, LEG_LENGTH = bipedal_dinos[NAME], float(LEG_LENGTH)
                result[NAME] = abs((STRIDE_LENGTH / LEG_LENGTH) - 1) * math.sqrt(LEG_LENGTH * g)

    # print(result)
    speed = sorted(((key,value) for key, value in result.items()), reverse=True)
    print(speed)

print(find_bipedal_speed('dataset1.csv','dataset2.csv'))

