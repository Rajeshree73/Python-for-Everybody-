fname = input("Enter the file name: ")
fh = open(fname)
dct = dict()
lst = list()
for line in fh:
    if line.startswith("From "):     
        line = line.rstrip().split()
        line = line[5]
        line = line[0:2]
        dct[line] =dct.get(line,0)+1
       
for value,key in dct.items():
    lst.append((value,key))
lst.sort()
for value,key in lst:
    print (value,key)        
