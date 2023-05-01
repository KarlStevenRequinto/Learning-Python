entered_weight = float(input("Input your weight: "))
entered_height = float(input("Input your height: "))

bmi = entered_weight / (entered_height*entered_height)

print("your bmi is: ", bmi)

if bmi < 18.5:
    print(f"your bmi is: {bmi}. You are underweight")
elif bmi <= 25:
    print(f"your bmi is: {bmi}. Your bmi is normal")
elif bmi <= 30:
    print(f"your bmi is: {bmi}. You are overweight")
elif bmi <= 35:
    print(f"your bmi is: {bmi}. You are obese")
else:
    print(f"your bmi is: {bmi}. You are clinically obese")
