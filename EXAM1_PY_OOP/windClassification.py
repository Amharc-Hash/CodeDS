print(" *** Wind classification ***")
inp = float(input('Enter wind speed (km/h) : '))
if inp < 0:
    print("!!!Wrong value can't classify.")
elif 0<=inp<52:
    print("Wind classification is Breeze.")
elif inp < 56:
        print("Wind classification is Depression.")
elif inp < 102:
        print("Wind classification is Tropical Storm.")
elif inp < 209:
        print("Wind classification is Typhoon.")
elif inp >= 209:
        print("Wind classification is Super Typhoon.")