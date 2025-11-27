import sys

if len(sys.argv) == 3:
    weight = float(sys.argv[1])
    height = float(sys.argv[2])
    print("User provided values:")
else:
    weight = 60
    height = 1.65
    print("No input given - using default values:")

bmi = weight / (height * height)

print("BMI Value:", bmi)
