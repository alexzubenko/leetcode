"""
there are two csv files
file1:
dino_name|dino_weight
---------------------
dino1    | 120
---------------------
dino2    | 110
---------------------
dino3    | 90

file2:
dino_name|dino_speed
--------------------
dino1    | 20
--------------------
dino2    | 30
--------------------
dino3    | 25

the result file should be

dino_name|dino_weight * dino_speed

"""


class Solution(object):
    def parse(self, file1, file2, file_result):
        result = {}
        with open(file1,'r') as file1:
            f1 = file1.readlines()
        with open(file2, 'r') as file2:
            f2 = file2.readlines()
        for line in f1:
            if 'dino_name' in line:
                continue
            dino1 = line.split(',')
            for line2 in f2:
                if 'dino_name' in line:
                    continue
                dino2 = line2.split(',')
                if dino1[0] == dino2[0]:
                    result[dino1[0]] = int(dino1[1]) * int(dino2[1])
        print(result)
        with open(file_result, 'w') as file_result:
            file_result.write('dino_name')
            file_result.write(',')
            file_result.write('dino_result')
            file_result.write('\n')
            for key in result.keys():
                file_result.write(key)
                file_result.write(',')
                file_result.write(str(result[key]))
                file_result.write('\n')


solution = Solution()
print(solution.parse('dino1.csv', 'dino2.csv', 'file.result.csv'))