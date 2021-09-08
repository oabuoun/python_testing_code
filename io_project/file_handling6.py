
file = open("readme.txt", "a+")

data = file.read()
print(data)

file.write("This is the new line 08\n")

file.writelines("This is the new line 08")

file.close()
