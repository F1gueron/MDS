'''
import re
text = input()
pattern = r"\b(\d{4})-(\d{2})-(\d{2})\b"
text = re.sub(pattern, r"\3.\2.\1", text, 1)
print(text)
'''

import re
text = input()
pattern = r"\b(\d{4})-(\d{2})-(\d{2})\b"
results = re.findall(pattern, text)
for g1, g2, g3 in results:
    formatted_date = f"{g3}.{g2}.{g1}"
    text = text.replace(f"{g1}-{g2}-{g3}", formatted_date)
print(text)
 
 