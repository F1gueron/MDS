import re
text = input()
pattern = r"\b(\d{4})-(\d{2})-(\d{2})\b"
text = re.sub(pattern, r"\3.\2.\1", text, 1)
print(text)
 