# Leap Year Exercise
print("\n\n Leap Year Exercise\n")

year = int(input("Which year do you want to check? "))

if (year % 4) == 0:
    if (year % 100) == 0:  # if year is divisible by 100
        if (year % 400) == 0:  # if year is divisible by 400
            print("This is a leap year.")
        else:  # if year is not divisible by 400
            print("This is not a leap year.")
    else:  # if year is not divisible by 100
        print("This is a leap year.")
else:  # if year is not divisible by 4
    print("This is not a leap year")