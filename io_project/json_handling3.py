import json

trainee = {'fname': 'Adam', 'lname': 'Smith', 'group': {'G1': 'Eng-94', 'G2': 'Cyber2'}, 'year': [2020, 2021], "subscribed": False, "courses": None}

print("This is the dictionary format")
print(trainee)

print("This is the JSON object")
trainee_json_object = json.dumps(trainee)
print(trainee_json_object)
