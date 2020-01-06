import math

print  "########\ntrapezio\n########"

B = int(input("B = "))
b = int(input("b = "))
h = int(input("h = "))

a = (B + b) * h /2
p = b + B + h + math.sqrt(b - B + h * h) 

print "Area = ",a,"\nPerimetro = ",p,
