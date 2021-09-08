colors = {'black', 'grey', 'red', 'blue', 'green'}

print(colors)

for i in colors:
    print(i)

colors.add('white')
print(colors)

colors.discard('grey')
print(colors)


print("================= Math & Sets =========")
colors1 = {'black', 'grey', 'red'}
colors2 = {'black', 'blue'}

print(colors1)
print(colors2)

print("Intersect: ", colors1 & colors2)
print("Union: ", colors1 | colors2)
print("Difference: ", colors1 - colors2)
print("Superset: ", colors1 > colors2)


items = set(("coffee", "tea", "black", "white"))
