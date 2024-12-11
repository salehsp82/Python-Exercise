t = int(input("Enter Second : "))

#t = 26741

m = (t % 3600) // 60
s = t % 60
h = t // 3600

print(h, ":", m, ":", s)