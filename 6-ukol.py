import re

with open('posta.txt', "r", encoding='utf-8') as soubor: 
    data = soubor.readlines()
    # print(data)

regularni_vyraz = re.compile(r"\d{3} +\d{2} +(\w| )+")
for line in data:
    vysledky = re.match(regularni_vyraz, line)
    if vysledky:
        print(vysledky)



