def welcome(id):
    print('welcome to Cyber Course')
    print('This is the beginning of the course, Week: ', id)
    return True

for i in range(0, 10):
    return_value = welcome(i)
    print(return_value)
