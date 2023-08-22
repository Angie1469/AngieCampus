age=int(input("Enter your Age:"))
if age < 16:
    print("Error.You must be 16 years old or older")
else:
    weight=float(input("Enter your weight in pounds:"))
    height=float(input("Enter your height in inches:"))
    weightkg=weight*0.45359237
    heightmt=height*0.0254
    BMI=weightkg/heightmt**2
    print(BMI)
    if BMI<18.5:
        print("Underweight")
    elif 18.5>BMI<24.9:
        print("Normal")
    elif 25.0>BMI<29.9:
         print("Overweight")
    elif BMI>30.0:
        print("Obese")