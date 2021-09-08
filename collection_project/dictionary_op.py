trainee = {'fname': 'Adam', 'lname': 'Smith', 'group': {'G1': 'Eng-94', 'G2': 'Cyber2'}, 'year': [2020, 2021]}

# or

trainee = dict(fname= 'Adam', lname= 'Smith', group=  {'G1': 'Eng-94', 'G2': 'Cyber2'}, year=  [2020, 2021])

print('fname: ', trainee['fname'])
print('lname: ', trainee['lname'])
print('group: ', trainee['group'])
print('year : ', trainee['year'])

trainee['fname'] = 'Mark'
print('fname: ', trainee['fname'])

print("Printing keys using a loop")
for i in trainee:
    print(i)

print("Printing keys using a loop with .keys()")
for i in trainee.keys():
    print(i)

print("Printing values using a loop")
for i in trainee.values():
    print(i)

print("Printing keys and values using a loop")
for key, value in trainee.items():
    print(key, ' : ',value)

print("Printing keys and values using a loop - Method 2")
for key in trainee:
    print(key, ' : ',trainee[key])
