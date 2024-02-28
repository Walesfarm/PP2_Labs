import re

with open('row.txt', 'r', encoding='utf-8') as file:
    text = file.read()
    
def camel_to_snake(text):
    return '_'.join(re.findall(r'[А-ЯA-Z](?:[а-яa-z]+|$)', text)).lower()

snake_case_text = camel_to_snake(text)
print(snake_case_text)