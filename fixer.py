import os
from pathlib import Path
import re
import uuid

BASE_DIR = Path(__file__).resolve().parent
TEMPLATE_DIR = os.path.join(BASE_DIR, 'templates')


def staticify_html(input_path, output_filename):
    with open(input_path, 'r', encoding='utf-8') as f:
        content = f.read()

    def replace_static(match):
        tag, attrs, url = match.groups()
        if url.startswith('http://') or url.startswith('https://'):
            return f'<{tag} {attrs}"{url}"'

        attrs = attrs.strip()
        if attrs.endswith('='):
            return f'<{tag} {attrs}"{{% static \'{url}\' %}}"'
        else:
            return f'<{tag} {attrs}="{{% static \'{url}\' %}}"'

    pattern_list = [
        r'<(link)([^>]*?href=)[\'"]([^\'"]+)[\'"]',
        r'<(script)([^>]*?src=)[\'"]([^\'"]+)[\'"]',
        r'<(img)([^>]*?src=)[\'"]([^\'"]+)[\'"]',
    ]

    for pattern in pattern_list:
        content = re.sub(pattern, replace_static, content)

    if '{% load static %}' not in content:
        content = '{% load static %}\n' + content

    content = content.replace('\\', '')

    output_path = os.path.join(TEMPLATE_DIR, output_filename)
    os.makedirs(os.path.dirname(output_path), exist_ok=True)

    with open(output_path, 'w', encoding='utf-8') as f:
        f.write(content)


def main():
    relative_input = input("HTML path: ").strip()
    input_path = os.path.join(BASE_DIR, relative_input)

    if not os.path.exists(input_path):
        print(f"❌ Fayl tapılmadı: {input_path}")
        return

    base_filename = os.path.basename(relative_input)
    name, ext = os.path.splitext(base_filename)
    unique_suffix = uuid.uuid4().hex[:10]
    output_filename = f"{name}-{unique_suffix}{ext}"

    staticify_html(input_path, output_filename)


if __name__ == '__main__':
    main()
