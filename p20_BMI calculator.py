# Problem20_BMI calculator"

weight= float(input("Enter weight :"))
height= float(input("Enter height :"))

BMI = (weight/(height**2))

if (BMI<18.5):
    status= "Underweight"
elif(18.5<=BMI<=24.9):
        status= "Normal weight"
elif(25<=BMI<=29.9):
        status= "Overweight"
else:
        status= "Obese"

print(f"\nYour height is {height}m, Your weight is {weight}Kg ")
print(f"Your BMI is {BMI}") 
print(f"\nYou are {status}.")       
