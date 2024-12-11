# تابع برای محاسبه مجموع ارقام
def sum_of_digits(number):
    sum_digits = 0
    while number > 0:
        sum_digits += number % 10
        number //= 10
    return sum_digits

num = int(input("enter number "))


total_sum = sum_of_digits(num)
print(total_sum)
