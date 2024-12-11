# محاسبه بزرگترین مقسوم علیه مشترک
def gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

num1 = int(input("enter number "))
num2 = int(input("enter number "))

greatest_common_divisor = gcd(num1, num2)
print(greatest_common_divisor)
