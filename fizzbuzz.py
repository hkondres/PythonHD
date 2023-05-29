# FizzBuzz
# If number is divisible by 3 write Fizz
# If number is divisible by 5 write Buzz
# If number is divisible by both then write FizzBuzz

for i in range(1,100):
    if i % 3 == 0 and i % 5 == 0:
        print(str(i) + " YES FizzBuzz")
    elif i % 5 == 0:
        print(str(i) + " Buzz")
    elif i % 3 == 0:
        print(str(i) + " Fizz")
    else:
        print(i)


