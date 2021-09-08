import json

with open('trainee.json', 'r') as file:
    trainee = json.load(file)

print(trainee)

for key, value in trainee.items():
    print(f"{key} = {value}")

trainee['year'] = [2020, 2021, 2022]

with open('trainee.json', 'w') as file:
    json.dump(trainee, file, indent = 4)
