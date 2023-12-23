import re
import html

with open('input.txt', 'r') as source_file:
    java_code = source_file.read()

cleaned_code = re.sub(r'<[^>]+>', '', java_code)

cleaned_code = html.unescape(cleaned_code)

with open('input.txt', 'w') as output_file:
    output_file.write(cleaned_code)
