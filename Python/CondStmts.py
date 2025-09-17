# If statement

Total_marks = 25

if Total_marks >= 9:
    print("You are pass..")

# If else statement

if Total_marks <= 9:
    print("You are pass..")
else:
    print("You are fail..")

# elif Statement

age = 25

if age <= 12:
    print("Child.")
elif age <= 19:
    print("Teenager.")
elif age <= 35:
    print("Young adult.")
else:
    print("Adult.")

#


age = int(input("Enter your age : "))
is_member = True

if age >= 60:
    if is_member:
        print("30% senior discount!")
    else:
        print("20% senior discount.")
else:
    print("Not eligible for a senior discount.")