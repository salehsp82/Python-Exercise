hw = float(input("enter hours_worked"))
hr = float(input("enter hourly_rate")) 

if hw <= 40:
    pay = hw * hr
else:
    regular_pay = 40 * hr
    overtime_pay = (hw - 40) * hr * 1.5
    pay = regular_pay + overtime_pay

print(pay)