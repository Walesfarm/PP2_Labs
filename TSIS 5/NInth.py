import re

with open('row.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    
spaced_text = re.sub(r'([а-яa-z])([А-ЯA-Z])', r'\1 \2', text)
print(spaced_text)