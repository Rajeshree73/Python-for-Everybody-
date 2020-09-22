fname = input("Enter the file name: ")
fh = open(fname)
count = 0

for line in fh:
    line = line.rstrip()
    if line.startswith('From '):
        count = count + 1
        words = line.split()
        emails = words[1]
        print(emails)
print("There were",count, "lines in the file with From as the first word")