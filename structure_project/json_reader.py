import json

with open("log-solution1.json") as file:
    json_data = json.load(file)
    print(json_data)
    print("-----------")
    print(type(json_data))
    print("-----------")

    for item in json_data:
        print(item["number2"])
