year = int(input('Enter the year: '))


def year_checker(year):
    if year % 4 == 0:
        if year % 100 == 0:
            if year % 400 == 0:
                print(f'{year} is a leap year')
            else:
                print(f'{year} not aleap year')
        else:
            print(f'{year} is a leap year')

    else:
        print(f'{year} is not a leap year')


year_checker(year)
