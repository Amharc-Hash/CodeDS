num = int(input("Input : "))
print()
for i in range(num):
    string = '*'*(i+1)
    string += ' '*(2*(num-i-1))
    string += '*'*(i+1)
    print(string)
for i in range(num-1):
    string = '*'*(num-i-1)
    string += ' '*(2*(i+1))
    string += '*'*(num-i-1)
    print(string)