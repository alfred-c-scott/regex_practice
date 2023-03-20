# regular expression practice

import re

regex_0 = ''

str_0 = '''
abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ

1234567890
 
. ^ $ * + ? { } [ ] / | ( )

Ha HaHa

911-825-9015
798.825.9015
6068259015
900-825-9015

email@email.com
corey.schafer@university.edu
blah.blah@university.edu
blah.blah9@university.edu
blah-blah@my-blah.net 

Mr. Schafer
Mr Smith
Ms Davis
Mrs. Robinson
Mr. T

cat
mat
fat
bat

https://www.google.com
http://coreyms.com
https://youtube.com
https://www.nasa.gov
'''

sentence = 'Start a sentence and then bring it to an end'

# printing a raw string
# ------------------------------------------------------
# print('\tTAB')
# print(r'\tTAB')

# ha_pattern_0 = re.compile(r'\bHa')
# matches = ha_pattern_0.finditer(str_0)
# for match in matches:
#     print(match)
#
# ha_pattern_1 = re.compile(r'\BHa')
# matches = ha_pattern_1.finditer(str_0)
# for match in matches:
#     print(match)
#
# beg_of_string_pattern = re.compile(r'^Start')
# matches = beg_of_string_pattern.finditer(sentence)
# for match in matches:
#     print(match)
#
# end_of_string_pattern = re.compile(r'end$')
# matches = end_of_string_pattern.finditer(sentence)
# for match in matches:
#     print(match)
#
# phone_pattern_0 = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d|\d\d\d\d\d\d\d\d\d\d')
# matches = phone_pattern_0.finditer(str_0)
# for match in matches:
#     print(match)
#
# phone_pattern_1 = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d|[89]00\d\d\d\d\d\d\d')
# matches = phone_pattern_1.finditer(str_0)
# for match in matches:
#     print(match)
#
# at_pattern = re.compile(r'[^b]at')
# matches = at_pattern.finditer(str_0)
# for match in matches:
#     print(match)
#
phone_pattern_2 = re.compile(r'\d{3}.\d{3}.\d{4}')
matches = phone_pattern_2.finditer(str_0)
for match in matches:
    print(match)
#
title_pattern = re.compile(r'M(r|s|rs)\.?\s[A-Z]\w*')
matches = title_pattern.finditer(str_0)
for match in matches:
    print(match)
#
# pattern = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d')
#
# with open('data.txt', 'r') as f:
#     contents = f.read()
#     matches = pattern.finditer(contents)
#
#     for match in matches:
#         print(match)

# pattern = re.compile(r'https?://(www\.)?(\w+)(\.com|\.gov)')
# matches = pattern.finditer(str_0)
# for match in matches:
#     print(match.group(0))
#     print(match.group(1))
#     print(match.group(2))
#     print(match.group(3))

# subbed_urls = pattern.sub(r'\2\3', str_0)
# print(subbed_urls)
