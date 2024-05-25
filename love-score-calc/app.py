name1 = input('name of the first person: ')
name2 = input('name of the second person: ')
combined_names = name1 + name2
combined_names.lower()

t = combined_names.count('t')
r = combined_names.count('r')
u = combined_names.count('u')
e = combined_names.count('e')
first_digit = t+r+u+e

l = combined_names.count('l')
o = combined_names.count('o')
v = combined_names.count('v')
e = combined_names.count('e')
second_digit = l+o+v+e

lovescore = str(first_digit)+str(second_digit)
lovescore = int(lovescore)

if (lovescore <= 10 or lovescore > 90):
    print(f'your lovescore is {lovescore}, this is not normal')
elif (lovescore > 10 and lovescore <= 40):
    print(f'your lovescore is {lovescore}, this is a weak kind of love')
elif (lovescore > 40 and lovescore <= 60):
    print(f'your lovescore is {lovescore}, this is ok love')
elif (lovescore > 60 and lovescore <= 90):
    print(f'your lovescore is {lovescore}, this is a true love')
