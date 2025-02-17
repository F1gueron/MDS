import re

text = input().strip()

p1 = r'([a-z]{2,})\.([a-z]{2,})\.(\d{4})@alumnos\.urjc\.es'
p2 = r'([a-z]{2,})\.([a-z]{2,})@urjc\.es'

p1_matches = re.findall(p1, text)
p2_matches = re.findall(p2, text)

if p1_matches:
    for m in p1_matches:
        print(f"alumno {m[1]} matriculado en {m[2]}")
if p2_matches:
    for m in p2_matches:
        print(f"profesor {m[0]} apellido {m[1]}")
