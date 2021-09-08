file = None
try:
    file = open("readme2.txt", "x")
except FileExistsError as file_exists_msg:
    print(file_exists_msg)
except Exception as exception_msg:
    print(exception_msg)
finally:
    file.close()
#data = file.read()
#print(data)

#file.close()
