def rec_show(underScore, sharps):           # underscore = number input - shaps unit
    print('_'*(underScore-sharps), end="")
    print('#'*sharps, end="")
    print()


def rec_pattern(number, row=0):
    if number > 0:
        if row < number:
            row += 1
            rec_show(number, row)
            rec_pattern(number, row)
    elif number == 0:
        print('Not Draw!')
    else:
        if row < abs(number):
            rec_show(abs(number), abs(number)-row)
            row += 1
            rec_pattern(number, row)


if __name__ == '__main__':
    number = int(input("Enter Input : "))
    rec_pattern(number)