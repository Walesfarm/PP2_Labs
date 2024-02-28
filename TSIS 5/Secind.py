import re

with open('row.txt', 'r', encoding='utf-8') as file:
    text = file.read()

pattern2 = re.findall(r'[a][b]{2,3}', text)
for match in pattern2:
    print(match)