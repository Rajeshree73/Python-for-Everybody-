fname = input("Enter file:")
fh = open(fname)
lst = list()
counts = dict()
bigcount = None
bigword = None
for line in fh:
    if line.startswith('From '):
        line = line.split()
        getwords = line[1]
        lst.append(getwords) 
for word in lst:
    counts[word] = counts.get(word,0)+1
for word,count in counts.items():
    if bigcount is None or count > bigcount:
        bigword = word
        bigcount = count
    
print(bigword, bigcount)
