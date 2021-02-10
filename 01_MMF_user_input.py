# 01 MMF - User Input

name = input("What is your name? ")
age = int(input("How old are you? "))

if age < 12:
    print()
    print("You are too young to attend this event")
else:
    print()
    print("Name: "+name)
    print("Age: {}".format(age))