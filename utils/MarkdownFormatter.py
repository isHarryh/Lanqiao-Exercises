# -*- coding: utf-8 -*-
# Copyright (c) 2024, Harry Huang
# @ MIT License
import os
import re

def format_file(src, dst):
    with open(src, 'r', encoding='UTF-8') as file:
        content = file.read()

    placeholders = {}
    index = 0

    def placeholder_replacer(match):
        nonlocal index
        placeholder = f"__PLACEHOLDER_START_{index}_PLACEHOLDER_END__"
        placeholders[placeholder] = match.group(0)
        index += 1
        return placeholder

    content = re.sub(r'(!?\[[^\]]*\]\([^\)]*\))', placeholder_replacer, content)

    content = re.sub(r'([\u4e00-\u9fff])([a-zA-Z0-9`!@#$%^&()\-+=\[\]{};:\'\"\\|<>,./?])', r'\1 \2', content)
    content = re.sub(r'([a-zA-Z0-9`!@#$%^&()\-+=\[\]{};:\'\"\\|<>,./?])([\u4e00-\u9fff])', r'\1 \2', content)

    content = re.sub(r' ([，。！？；：》）”’])', r'\1', content)
    content = re.sub(r'([，。！？：；（《“‘]) ', r'\1', content)

    content = re.sub(r'([\u4e00-\u9fff，。！？：；（《“‘》）”’])\$', r'\1 $', content)
    content = re.sub(r'\$([\u4e00-\u9fff，。！？：；（《“‘》）”’])', r'$ \1', content)

    for placeholder, original in placeholders.items():
        content = content.replace(placeholder, original)

    with open(dst, 'w', encoding='UTF-8') as file:
        file.write(content)

if __name__ == '__main__':
    for root, _, files in os.walk('.'):
        for file_name in files:
            if file_name.endswith('.md'):
                file_path = os.path.join(root, file_name)
                print(f"Formatting file: {file_path}")
                format_file(file_path, file_path)
