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

Mr. Schafer
Mr Smith
'''

sentence = 'Start a sentence and then bring it to an end'
# printing a raw string
# ------------------------------------------------------
# print('\tTAB')
# print(r'\tTAB')

email_pattern = re.compile(r'email@email\.com')
matches = email_pattern.finditer(str_0)
for match in matches:
    print(match)

ha_pattern_0 = re.compile(r'\bHa')
matches = ha_pattern_0.finditer(str_0)
for match in matches:
    print(match)

ha_pattern_1 = re.compile(r'\BHa')
matches = ha_pattern_1.finditer(str_0)
for match in matches:
    print(match)

beg_of_string_pattern = re.compile(r'^Start')
matches = beg_of_string_pattern.finditer(sentence)
for match in matches:
    print(match)

end_of_string_pattern = re.compile(r'end$')
matches = end_of_string_pattern.finditer(sentence)
for match in matches:
    print(match)

phone_pattern_0 = re.compile(r'\d\d\d[-.]\d\d\d[-.]\d\d\d\d|\d\d\d\d\d\d\d\d\d\d')
matches = phone_pattern_0.finditer(str_0)
for match in matches:
    print(match)

phone_pattern_1 = re.compile(r'[89]00[-.]\d\d\d[-.]\d\d\d\d|[89]00\d\d\d\d\d\d\d')
matches = phone_pattern_1.finditer(str_0)
for match in matches:
    print(match)
