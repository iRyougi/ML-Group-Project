weight = float(input("Enter your weight in kilos: "))
height = float(input("Enter your height in centimeters: "))

BMI = weight / (height/100)**2

print(f"Your weigh {weight}kg and you are {height}cm tall. This gives you BMI index of {BMI}")