print(' *** Wind classification ***')
inp = float(input('Enter wind speed (km/h) : '))
if 0<=inp<52:
    print('Wind classification is Breeze.')
elif 52<=inp<56:
    print('Wind classification is Depression.')
elif 56<=inp<102:
    print('Wind classification is Tropical Storm.')
elif 102<=inp<209:
    print('Wind classification is Typhoon.')
elif inp>=209:
    print('Wind classification is Super Typhoon.')
else:
    print('!!!Wrong value can\'t classify.')
