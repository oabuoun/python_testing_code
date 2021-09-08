import json

with open('trainee.json', 'r') as file:
    trainee = json.load(file)

print(trainee)

for key, value in trainee.items():
    print(f"{key} = {value}")
