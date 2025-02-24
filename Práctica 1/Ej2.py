import re
text = input()
pattern = r"\b((E[- ]?)?[0-9]{4}[- ]?[A-Z]{3})\b"

results = re.findall(pattern, text)

for match in results:
    if match[0] == "":
        print(match)
    else:
        print(match[0])