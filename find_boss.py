import operator

f = open("salaries.txt", "r")
salaries = f.read()
f = open("names.txt", "r")
names = f.read()

salaries = salaries.split(",")
names = names.split(",")

set_names = set(names)

print(len(set_names))
print(len(names))

dictionar = {}
for k in range(len(names)):
    if names[k] in dictionar:
        result = dictionar[names[k]] + int(salaries[k])
        dictionar[names[k]] = result
    else:
        dictionar[names[k]] = int(salaries[k])

print(dictionar)
print(max(dictionar.items(), key=operator.itemgetter(1))[0])