import re

text = input()
#print(text)
#text = "2022-02-07 01:14:28.313  INFO 1174086 --- [main] drfp.Main            : Starting Main v0.1-SNAPSHOT using Java 17.0.1 on raul2-ubuntu with PID 1174086 started by rmartin"
regex = r"\d{4}-\d{2}-\d{2} \d{2}:\d{2}:\d{2}\.\d{3}\s+(\w+)\s+(?:\d+)\s+---\s+\[(\w+)\]\s+(?:\w*\.)*(\w+)\s+:\s+(.+)"
match = re.findall(regex, text)
if match:
    for m in match:
        print(f'"{m[0]}","{m[1]}","{m[2]}","{m[3]}"')
