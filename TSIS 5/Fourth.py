import re

with open('row.txt', 'r', encoding='utf-8') as file:
    text = file.read()

pattern4 = re.findall(r'[А-ЯA-Z][а-яa-z]+', text)
for match in pattern4:
    print(match)