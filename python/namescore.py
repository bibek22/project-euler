namefile = open("p022_names.txt", 'r')
names = namefile.read()
names = names.split("[\"")[-1].split("\"]")[0]
names = names.split("\",\"")
names.sort()
grandTotal = 0
for name in range(0, len(names)):
    namescore = 0
    for letter in names[name]:
        print ord(letter)
        namescore += ord(letter)-64
    grandTotal += namescore*(name+1)

print grandTotal
    