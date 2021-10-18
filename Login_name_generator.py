print("enter your firstname, lastname, and year you were born: ")
values = input().split()
first = values[0]
last = values[1]
number = int(values[2])

if len(last) > 5:
    last = last[:5]

print("Your login name: {}{}{}".format(last, first[0], number % 100))
