import json

trainees = [{'fname': 'Adam1', 'lname': 'Smith', 'group': {'G1': 'Eng-94', 'G2': 'Cyber2'}, 'year': [2020, 2021], "subscribed": False, "courses": None}, {'fname': 'Adam', 'lname': 'Smith', 'group': {'G2': 'Eng-94', 'G2': 'Cyber2'}, 'year': [2020, 2021], "subscribed": False, "courses": None}]

with open('trainees.json', 'w') as file:
    json.dump(trainees, file, indent = 4)

with open('trainees.json', 'r') as file:
    trainees = json.load(file)

print(trainees)
