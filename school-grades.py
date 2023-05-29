# Write a program that asks user for a score from 1-100 and then
# displays their grade according to following criteria:
#  90 -100 = A
#  80 - 89 = B
#  70 - 79 = C
#  60 - 69 = D
#     < 60 = F

score = input(f"Please enter your test score (1-100): ")
score = int(score)

if score >= 90:
    age = int(input("What is your age? "))
    if age < 10:
        print("You are amazing and you deserve an A+ !!! ")
    else:
        print("Your grade is A ")
elif score >= 80:
    age = int(input("What is your age? "))
    if age < 10:
        print("You are really great for your age and you deserve a B+ !!! ")
    else:
        print("Your grade is B ")
elif score >= 70:
    print("Your grade is C ")
elif score >= 60:
    print("Your grade is D ")
else:
    print("Your score is F ... I'm sorry but you failed your test :( ")
