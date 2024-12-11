def repeat_digits(number):
    number_str = str(number)
    for digit in number_str:
        digit_value = int(digit)
        repeated_digits = digit * digit_value
        print(repeated_digits)

num = int(input("enter number "))

repeat_digits(num)
