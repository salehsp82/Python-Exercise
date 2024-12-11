import math

a = 1
b = 6
c = 5

d = (b ** 2) - (4 * a * c)

r1 = (b + math.sqrt(d)) / (2 * a)
r2 = (b - math.sqrt(d)) / (2 * a)

print(r1)
print(r2)