import re

with open('row.txt', 'r', encoding='utf-8') as file:
    text = file.read()

pattern1 = re.findall(r'[a][b]*', text)
for match in pattern1:
    print(match)