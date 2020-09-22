hrs = input("Enter Hours:")
h = float(hrs)
rate = input("Enter Rate per Hour: ")
r = float(rate)
if h<40:
    pay = h*r
else:
    pay = (h*r)+ (h-40.0)*0.5*r
   
print(pay)