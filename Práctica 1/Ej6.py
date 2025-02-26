import re

text = input().strip()
regex = r"^\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}\s+(\w+)\s+(?:\d+)\s+---\s+\[(\w+)\]\s+(?:[\w]\.)*([\w]+)\s+:\s+(.+)$"
match = re.fullmatch(regex, text)
if match:
    level = match.group(1)
    thread = match.group(2)
    class_name = match.group(3)
    message = match.group(4)
    print(f'"{level}","{thread}","{class_name}","{message}"')
