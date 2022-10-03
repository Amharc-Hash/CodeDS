def multiple(x, y):
    return x * y


def adder(x, y):
    return x + y

print("*** multiplication or sum ***")
num1, num2 = map(int, input('Enter num1 num2 : ').split())
ans = 0

if multiple(num1, num2) > 1000:
    ans = adder(num1, num2)
elif multiple(num1, num2) <= 1000:
    ans = multiple(num1, num2)

print(f'The result is {ans}')
