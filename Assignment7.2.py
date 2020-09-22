# Use the file name mbox-short.txt as the file name
fname = input("Enter file name: ")
fh = open(fname)
count = 0
avg = 0
for line in fh:
    if not line.startswith("X-DSPAM-Confidence:") : continue
    count = count+1
    num =  float(line[20:])
    avg = (avg + num)
    
print("Average spam confidence:",avg/count)
