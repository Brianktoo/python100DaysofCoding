#simple program to calculate BMI
print('FIND YOUR BMI')
weight= input('Please enter your weight in (kgs): ')
height= input('Please enter your height in (m): ')

weight= float(weight)
height= float(height)

BMI= weight/(height*height)
BMI=int(BMI)

print(f'Your BMI is {BMI}')