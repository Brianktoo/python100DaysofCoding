# simple program to calculate BMI
print('FIND YOUR BMI')
weight = input('Please enter your weight in (kgs): ')
height = input('Please enter your height in (m): ')

weight = float(weight)
height = float(height)
BMI = weight/(height*height)
BMI = int(BMI)

print(f'Your BMI is {BMI}')


def weight_checker(BMI):
    if (BMI < 18.5):
        print('your are underweight')
    elif (BMI >= 18.5 and BMI < 25):
        print('your have normal weight')
    elif (BMI >= 25 and BMI < 30):
        print('your are slightly overweight')
    elif (BMI >= 30 and BMI < 35):
        print('your are obese')
    elif (BMI > 35):
        print('your are clinically obese')


print(weight_checker(BMI))
