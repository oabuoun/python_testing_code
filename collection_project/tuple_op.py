trainee = ("Adam", "Smith", "Eng-94", 2021)

print(trainee)
print(trainee[0])
print(trainee[2])

for i in trainee:
    print(i)

i = 0

print("\nThis is the tuple using while\n")
while i < len(trainee):
    print(trainee[i])
    i += 1

print("\nThis is to extract the values")
fname = trainee[0]
lname = trainee[1]
group = trainee[2]
year  = trainee[3]

print("fname: ", fname)
print("lname: ", lname)
print("group: ", group)
print("year : ", year)

print("\nThis is to extract the values using a new method")
fname , lname, group , year  = trainee

print("fname: ", fname)
print("lname: ", lname)
print("group: ", group)
print("year : ", year)
