import re

with open('row.txt', 'r', encoding='utf-8') as file:
    text = file.read()

split_text = re.findall('[А-ЯA-Z][^А-ЯA-Z]*', text)
for match in split_text:
    print(match)