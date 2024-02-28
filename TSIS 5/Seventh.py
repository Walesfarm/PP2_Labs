import re

with open('row.txt', 'r', encoding='utf-8') as file:
    text = file.read()

def snake_to_camel(text):
    return ''.join(word.title() for word in text.split('_'))

camel_case_text = snake_to_camel(text)
print(camel_case_text)