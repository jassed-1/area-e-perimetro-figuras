import math

print "########\ntriangulo\n########"

b = int(input("b = "))
h = int(input("a = "))

a = (b * h) / 2
p = math.sqrt(b * b + h * h) + h + b

print "Area = ",a,"\nPerimetro = ",p,

