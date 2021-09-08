
file = open("readme.txt", "r")

data = file.readline(5)

while data != '':
    print(data)
    data = file.readline(5)

file.close()
