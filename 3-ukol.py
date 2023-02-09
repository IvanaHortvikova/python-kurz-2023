import json
with open('body.json', encoding='utf-8') as soubor:
    data = json.load(soubor)[0]
    new_dict = {}
    for key, val in data.items():
        if val >= 60:
            new_dict[key] = 'Pass'
        else:
            new_dict[key] = 'Fail'
with open('prospech.json', 'w') as soubor:
    json.dump(new_dict, soubor, indent=4)

