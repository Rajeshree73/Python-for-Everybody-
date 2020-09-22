score = input("Enter Score: ")
sco = float(score)
if sco>=0.9:
    print("A")
elif sco>=0.8:
    print("B")
elif sco>= 0.7:
    print("C")
elif sco>= 0.6:
    print("D")
elif sco< 0.6:
    print("F")
else:
    print("Error")