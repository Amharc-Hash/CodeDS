input_num = int(input("Enter Input : "))
print('.'*(input_num+1)+'#'+'+'*(input_num+2))
for i in range(1, input_num+1):
    print('.'*((input_num+1) - i) + '#'*(i+1) + '+' + '#'*(input_num) + '+')
print('#'*(input_num+2)+'+'*(input_num+2))
print('#'*(input_num+2)+'+'*(input_num+2))
for i in range(1,input_num+1):
    print('#'+'+'*(input_num)+'#'+'+'*(input_num+2 - i)+'.'*i)
print('#'*(input_num+2)+'+'+'.'*(input_num+1))