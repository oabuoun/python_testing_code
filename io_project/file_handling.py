
file = open("readme.txt", "r")

data1 = file.read(10)
print(data1)

data2 = file.read(10)
print(data2)

file.close()
