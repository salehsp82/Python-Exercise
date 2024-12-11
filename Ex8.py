# تابع برای محاسبه معدل
def calculate_gpa(grades, credits):
    total_points = sum([grade * credit for grade, credit in zip(grades, credits)])
    total_credits = sum(credits)
    gpa = total_points / total_credits
    return gpa

# دریافت اطلاعات از کاربر
student_id = input("شماره دانشجویی را وارد کنید: ")
num_courses = int(input("تعداد دروس را وارد کنید: "))

grades = []
credits = []

for i in range(num_courses):
    grade = float(input(f"نمره درس {i+1} را وارد کنید: "))
    credit = int(input(f"تعداد واحد درس {i+1} را وارد کنید: "))
    grades.append(grade)
    credits.append(credit)

# محاسبه معدل
gpa = calculate_gpa(grades, credits)

# نمایش معدل و شماره دانشجویی
print(f"شماره دانشجویی: {student_id}")
print(f"معدل: {gpa:.2f}")
