
# Python program to illustrate
# while loop

# nr.1 simple loop

# count = 0
# while count < 10:
#     count += 1
#     print("Hello Geek")

# nr.2 more complex loop

i = 0
a = 'geeksforgeeks'

while i < len(a):
    if a[i] == 'e' or a[i] == 's':
        i += 1
        continue

    print('Current Letter :', a[i])
    i += 1
