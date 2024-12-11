numbers = []

print("اعداد غیر از صفر را وارد کنید. برای خاتمه وارد کردن اعداد، عدد صفر را وارد کنید.")

while True:
    num = float(input("عدد را وارد کنید: "))
    if num == 0:
        break
    numbers.append(num)

if len(numbers) == 0:
    print("هیچ عددی وارد نشده است.")
else:
    average = sum(numbers) / len(numbers)
    print(f"میانگین اعداد وارد شده: {average:.2f}")
