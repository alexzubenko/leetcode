"""

Parse the log


"""

import re
import os

class Solution:
    # this function will coun the errors for systemd and for ntpd
    def parser(self, file_path):
        with open(file_path) as file:
            result = file.readlines()
            systemd_counter = 0
            ntpd_counter = 0
        for line in result:
            result = line.split(' ',5)
            if re.match(r'systemd', result[4]) and re.match(r'Failed', result[5]):
                systemd_counter +=1
            elif re.match(r'ntpd', result[4]) and re.match(r'Failed', result[5]):
                ntpd_counter +=1

        return systemd_counter, ntpd_counter
    # this function should combine the errors by cause and show the numbers
    # of errors
    # this funcion is not very good in case of huge file
    def parser_advanced(self, file_path):
        if not os.path.isfile(file_path):
            print("wrong path")
            return
        result = {}
        with open(file_path) as file:
            for line in file.readlines():
                cause = line.split()[4]
                if cause in result:
                    result[cause] +=1
                else:
                    result[cause] = 0
        return result

    # write a function which do the same as above
    # but it should use less memory
    # the above function use readlines which put entire file
    # to the memory
    # here we shoulf use the readline instead

    def parser_memory_save(self, file_path):
        if not os.path.isfile(file_path):
            print("{} does not exists".format(file_path))
        result = {}
        with open(file_path) as file:
            for line in file:
                cause = line.split()[4]
                if cause in result:
                    result[cause] +=1
                else:
                    result[cause] = 0
        return result

    # def parser_memory_save(self, file_path):
    #     if not os.path.isfile(file_path):
    #         print("{} does not exists".format(file_path))
    #     result = {}
    #     with open(file_path) as file:
    #         line = file.readline()
    #         while line:
    #             cause = line.split()[4]
    #             if cause in result:
    #                 result[cause] +=1
    #             else:
    #                 result[cause] = 0
    #             line = file.readline()
    #     return result




sol = Solution()
print(sol.parser_memory_save("C:\Brother\syslog.txt"))
# print(sol.parser("C:\Brother\syslog.txt"))
# # result = sol.parser_advanced("C:\Brother\syslog.txt")
# result = sol.parser_memory_save("C:\Brother\syslog.txt")
# for key, value in result.items():
#     print('{}:{}'.format(key, value))
