def add(*args):
    total = 0
    for i in args:
        total+=i
    return total


def subtract(x , y):
    return x - y 

def multiply(*args):
    total = 1
    for i in args:
        total*=i
    return total 


def division(x , y):
    if y == 0:
        raise ZeroDivisionError
    return x/y

def expo(x , y):
    if y == 0:
        return 1
    elif y == 1:
        return x
    else:
        return x**y
    

def root(x , y , epsioln):

    low = 0
    if x <1:
        high = 1
    else:
        high = x

    num = (low+high) /2

    while abs(num**y - x) >= epsioln:
        if num**y > x:
            high = num
        else:
            low = num
        num = (low+high) /2

    return num 

# print(root(64 , 6 , 0.000001))


def split_numbers(word):
    numbers = '0123456789'
    nums = []
    math_ops = []
    temp_nums = ''
    temp_ops = ''
    for i in range(len(word)):
        if word[i] not in numbers:
            temp_ops+=word[i]
            if temp_nums !='':
                nums.append(temp_nums)
            temp_nums = ''
        else:
            temp_nums+=word[i]
            if temp_ops != '':
                math_ops.append(temp_ops)
            temp_ops = ''

    nums.append(temp_nums)
    return nums , math_ops

# word = '2+12-3**6//4'
# print(split_numbers(word))

def main():

    print(96*'=')
    print( '='*30 ,  ' WELCOME TO MY SIMPLE CALCULATOR ' , '='*30)
    print(96*'=')

    while True:
        print(96*'=')
        print('choose operation')
        print('1-addition')
        print('2-subtraction')
        print('3-multiplication')
        print('4-divsion')
        print('5-power')
        print('6-root')
        print('7-exit')

        oper = int(input())

        if oper in range(1, 5 , 1):
            num1 = int(input('num1: '))
            num2 = int(input('num2: '))
            if oper == 1:
                print(add(num1 , num2))
            elif oper == 2 :
                print(subtract(num1 , num2))
            elif oper == 3:
                print(multiply(num1 , num2))
            elif oper == 4:
                print(division(num1 , num2))
        elif oper == 5:
            num = int(input('base: '))
            pwr = int(input('power: '))
            print(expo(num , pwr))
        elif oper == 6:
            num = float(input('number: '))
            root_pwr = int(input('root power: '))
            epsilon = float(input('epsilon: '))

            print(root(num , root_pwr , epsilon))
        
        elif oper == 7:
            break
        
        else:
            print('please choose from the list above')
    

# main()