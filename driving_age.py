age = int(input("Please enter your age:"))
if age < 7 or age > 60:
    print("You are not allowed to drive")
elif age == 18:
    print("You will have to give test to decide")
else:
    print("You are allowed to drive")
