import re


text_to_search = """

800-900-3224
800.433.4455
500*445*4455

172.34.53.255
192.168.1.1
10.22.55.322
5555.77.88.999

"""

phone_pattern = re.compile(r'\b[895]\d{2}[.\*-]\d{3}[.\*-]\d{4}\b')

ip_class_a_pattern = re.compile(r'\b(172|10)\.\d{1,3}\.\d{1,3}\.\d{1,3}\b')
ip_class_c_pattern = re.compile(r'\b192\.\d{1,3}\.\d{1,3}\.\d{1,3}')

parse_result = phone_pattern.finditer(text_to_search)

parse_ip_result = ip_class_c_pattern.finditer(text_to_search)

for match in parse_result:
    print(match)

for match in parse_ip_result:
    print(match)