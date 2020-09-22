fname = input("Enter the file name:")
fh = open(fname)
lst = list()
for line in fh:
    words = line.rstrip()
    getword = words.split()
    for eachword in getword:
        if eachword in lst:continue
        else: lst.append(eachword)
lst.sort()
print(lst)
