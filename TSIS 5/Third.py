import re

with open('row.txt', 'r', encoding='utf-8') as file:
    text = file.read()

pattern3 = re.findall(r'[а-яa-z]+_[а-яa-z]+', text)
for match in pattern3:
    print(match)