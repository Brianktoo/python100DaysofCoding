print('welcome to the tip calcultor')
bill = float(input('what is the total bill'))
tip = int(input('how much tip would you like to give? 10,12 or 15'))
people = int(input('how many people to split the bill'))

bill_with_tip = tip/100*bill + bill
print(bill_with_tip)

bill_per_person = round(bill_with_tip/int(people))
print(f'each person should pay{bill_per_person}')
