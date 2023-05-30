# FizzBuzz
# If number is divisible by 3 write Fizz
# If number is divisible by 5 write Buzz
# If number is divisible by both then write FizzBuzz
import time

choice = int(input("What is your number of choice? "))

def function(choice):
    for i in range(1,choice):
        if i % 3 == 0 and i % 5 == 0:
            print(str(i) + " YES... FizzBuzz!")
        elif i % 5 == 0:
            print(str(i) + " Buzz")
        elif i % 3 == 0:
            print(str(i) + " Fizz")
        else:
            print(i)

print("...about to run the program...")

for i in range (1,6):
    time.sleep(1)
    print(".")

function(choice)



