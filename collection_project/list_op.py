colors = ['black', 'red', 'green', 'blue']

print(colors)

print(colors[0])

colors[0] = "White"
colors.append("Orange")

colors.remove("green")


print("colors.index = ", colors.index("White"))
colors.sort()
print("colors.index = ", colors.index("White"))


for color in colors:
    print(color)

print("red in colors: ", "red" in colors)
print("grey in colors: ", "grey" in colors)

print("Slice: ", colors[0:2])

print("---------------------------")
items = ['black', 1.5, True, 'Red']

for item in items:
    print(item)

print(len(item))
