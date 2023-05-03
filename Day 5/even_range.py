
for number in range(1, 101):
    if number % 3 == 0 and number % 5 == 0:
        print("divisible by 3 & 5")
    elif number % 3 == 0:
        print("divisible by 3")
    elif number % 5 == 0:
        print("divisible by 5")
    else:
        print(number)