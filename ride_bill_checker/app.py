# complete illustraation of mutiples conditions and nested if staement
height = int(input('Enter you height in cm: '))
amout = 0
want_pictures = 3

if (height >= 120):
    print('you can ride')
    age = int(input('Enter your age in years: '))
    if (age < 12):
        amout = amout+5
        print(f' your bill is $ {amout}')
    elif (age >= 12 and age < 18):
        amout = amout+7
        print(f'your bill is $ {amout}')
    elif (age >= 18):
        amout = amout+12
        print(f' your bill is $ {amout}')
    picture = input('want to take pictures, y or n: ')

    if (picture == 'y'):
        total_bill = amout+3
        print(f' total bill is $ {total_bill}')
    else:
        print(f' total bill is $ {amout}')

else:
    print('hopps!, you cant ride, you have to grow taller to be allowed to can ride')
