print('BMI_Checker')
# Enter your height in meters e.g., 1.55
height = float(input())
# Enter your weight in kilograms e.g., 72
weight = int(input())

height = float(height)
weight = float(weight)
xBMI = (weight / (height ** 2))
BMI= round(xBMI)
if BMI < 35:
 if BMI < 18.5:
  print(f'Your BMI is {BMI}, you are underweight.')
 elif BMI < 25:
  print(f'Your BMI is {BMI}, you have a normal weight.')
 elif BMI < 30:
  print(f'Your BMI is {BMI}, you are slightly overweight.')
 else:
  print(f'Your BMI is {BMI}, you are obese.')
else: 
 print(f'Your BMI is {BMI}, you are clinically obese.')
