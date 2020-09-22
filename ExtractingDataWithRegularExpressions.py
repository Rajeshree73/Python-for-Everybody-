import re
fname = input('Enter the file name: ')
fh = open(fname)
lst = list()
#count = 0
sum = 0
for line in fh:
	line = line.rstrip()
	numbers = re.findall('[0-9]+', line)
	lst = lst + numbers
#print(lst)	
for getsum in lst:
	sum = sum + int(getsum)
	#count = count + 1
#print(sum,count)
print(sum)
