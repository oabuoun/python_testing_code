
try:
    with open("readme.txt", "r") as file:
        data = file.read()
        print(data)
except Exception as e:
    print(e)
