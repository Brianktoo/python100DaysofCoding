print('welcome to the treasure island, \nyour mission is to find treasure\n')
lr = input('Enter, left or right?: ')
lr = lr.lower()
if (lr == 'left'):
    sw = input('Enter, swim or wait: ')
    sw = sw.lower()
    if (sw == 'wait'):
        door = input('which door?, enter  red or rellow or  blue: ')
        door = door.lower()
        if (door == 'red'):
            print(f'congralulation You Win!{door} door is the way to treasure')
        else:
            print('game over!')
    else:
        print('game over!')
else:
    print('game over!')
