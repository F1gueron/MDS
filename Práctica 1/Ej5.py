import re

pattern = r"\b(?:C\/|Calle)\s([A-ZÑÁÉÍÓÚÜ][a-záéíóúñü]{0,}),?\s{1,}(?:(?:N|n)(?:º)|(?:N|n)\s?(?=\d))?\s{0,}(\d+)\s{0,},\s{0,}(\d{5})\b"
text = input()

matches = re.findall(pattern, text)
for street_name, number, postal_code in matches:
    print(f"{postal_code}-{street_name}-{number}")