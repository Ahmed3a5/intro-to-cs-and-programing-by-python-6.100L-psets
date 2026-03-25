

## the squqre root function beacuse the all factors of a number is less than the square root 
## so we use the square root to loop below it 
def find_sqr_root(x):
    ## bisection algorithm 
    ## make the epsiolon
    ## IF x is zero we return zero
    if x == 0:
        return 0
    
    epsilon = 0.00001
    ## if the x is less than 1 then the high is 1
    if x < 1:
        high = 1
    ## or the high is the x 
    else: 
        high = x
    low = 0
    ## make the intial guess 
    guess = (low+high) / 2
    ## iterate while the guess power of 2 minus the number is greater than the epsiolon
    while abs(guess**2 - x) >= epsilon:
        ## if the guess power is great than x then the correct guess is in the first half 
        ## so make the new high equal the guess 
        if guess**2 > x:

            high = guess
        ## if not then the correct nuber in the second half and make the low equal to guess 
        else:
            low = guess
        ## make a new gueess
        guess = (low+high) / 2
    
    return guess

def split_equation(word):
    """
    word is a string of the trinomial equatation x2+bx+c
    return the numbers which is in b and c 
    the first number in the list is b or coefficiant 
    the second number in the list is the c or constant 
    """
    temp =''
    numbers = []
    letters = 'qwertyuioplkjhgfdsazxcvbnm'
    ## iterate throught the equation from the bx+c 
    ## the x**2 take first 3 bytes in qquation so we start at 4 
    for i in range(4 , len(word)):
        if word[i] in letters:
            remain = word[i+1:]
            if remain:
                numbers.append(int(remain))
            else:
                numbers.append(0)
            break
        else:
            temp+=word[i]
    
    if temp == '+':
        numbers.append(1)
    elif temp == '-':
        numbers.append(-1)
    else:
        numbers.append(int(temp))
    
    if len(numbers) < 2:
        numbers.append(0)

    numbers[0] , numbers[1] = numbers[1] , numbers[0]
    return numbers

# word = 'x**2-4x'
# print(split_equation(word))

def find_all_factors(x):
    """
        this function is take an integer x and return a list of all possible factors 
    """
    if x == 0:
        raise ValueError('0 have infinte factors ')
    ## if the x less than 0 we take the absolite value
    if x < 0:
        x = abs(x)
    ## intialize the maximum  iteration of the loop by find the sqaure root and intialize the list 
    factors = []
    max_factor = round(find_sqr_root(x))
    ## iterate throught the max factor
    for i in range(1 , max_factor+1):
        ## then we make the integer divsion of x to all possible numbers < square root of x 
        temp = x // i
        ## then we conditon if this integer divsion wen multiplied by i will give us the x or not
        ## if give us the x then this is afactor of the x 
        if temp*i == x:
            ## if the temp not append in the list 
            ## we append it to the list with the number that the temp multiplide by to give the x
            ## so this make a pair of 2 factors of x
            factor = (temp , i)
            if factor not in factors:
                factors.append(factor)
    return factors
            
# word = 'x**2+10x-21'
# numbers = split_equation(word)
# print(find_all_factors(numbers[0]))

def find_larger(nums):
    """
    find the largest and smaller  number in the factor tuples  
    """
    ## intialize variables 
    largest = nums[0]
    smaller = nums[0]
    ## iterate through the tuples 
    for i in range(len(nums)):
        ## if the current number in tuple larger than the largest then make the largest eqaual it 
        if nums[i] > largest:
            largest = nums[i]
        ## if the current number less than the smaller we make it the smaller 
        elif nums[i] < smaller:
            smaller = nums[i]
    
    return largest ,smaller

# nums = (2,2)
# larger , smaller = find_larger(nums)
# print(f'the larger {larger}' ,',' , f'the smaller {smaller}')

def find_suitable_factors(string):
    """
        string is the equation in form of x2+bx+c
        return the factor form of the equartion 
    """
    ## intialize or variables and split the equation 
    variable = string[0]
    numbers = split_equation(string) ## return a list first num is coefficiant and second is constant 
    coeficiant = numbers[0]
    constants = numbers [1]
    ## find all the factors for the number 
    if constants == 0:
        if coeficiant>=0:
            mes = f'{variable}({variable}+{coeficiant})'
        else:
            mes = f'{variable}({variable}{coeficiant})'
        return mes
    
    factors = find_all_factors(numbers[1]) 

    if coeficiant == 0:
        if constants > 0:  ## constanats must be negative to factorized 
            mes = 'can not be factorized'
        else:
            num = find_sqr_root(abs(constants))
            num = round(num)
            if num*num == abs(constants):
                mes = f'({variable}-{num})({variable}+{num})'
            else:
                mes ='can not be factorized '
    ## then condition if the 2 numbers is negative or one negative and other positive 
    elif coeficiant < 0 and constants > 0:
        ## if the coefficaint negative and the constant positive 
        ## then the larger number is is positive
        ## we iterate through all factors 
        for factor in factors:
            ## find the large and small numbers 
            larger , smaller = find_larger(factor)
            ## see if the larger minu the smaller equal the constant if then this is the suitable factors
            if -larger-smaller == coeficiant:
                mes = f'({variable}-{larger})({variable}-{smaller})'
                break
            else:
                mes = 'the equation not factorize '

    elif coeficiant < 0 and constants< 0 :
        ## if the 2 numbers is negative the the larger number is negative and smaller is positive 
        for factor in factors:
            larger , smaller = find_larger(factor)
            ## we see if the smaller minus larger is equal the constant 
            if smaller-larger == coeficiant:
                mes = f'({variable}-{larger})({variable}+{smaller})'
                break
            else:
                mes = 'the equation not factorize '

    elif coeficiant > 0 and constants < 0 :
        ## if the constant is negative then the 2 numbers is negative 
        for factor in factors:
            larger , smaller = find_larger(factor)
            if larger - smaller == coeficiant:
                mes = f'({variable}+{larger})({variable}-{smaller})'
                break
            else:
                mes = 'the equation not factorize '

    elif coeficiant > 0 and constants > 0:
        ## if the 2 numbers positive then the addition of the 2 numbers must equal the constant 
        for factor in factors:
            larger , smaller = find_larger(factor)
            if larger+smaller == coeficiant:
                mes = f'({variable}+{larger})({variable}+{smaller})'
                break
            else:
                mes = 'the equation not factorize '
    else:
        mes = 'the equation not factorize '

    
    return mes


# equation = 'x**2'
# print(find_suitable_factors(equation))


def main():
    letters = 'qwertyuioplmkjnhbgvfcdxsza'
    while True:
        print(102*'=')
        print(10*'=' , 'WELCOME TO SIMPLE second degree trinomial equation  FACTORization' , 25*'=')
        print(102*'=')

        try:
            print('1-find the equation factors')
            print('2-EXIT')
            choice = int(input())

            if choice == 1:
                print('enter second degree equation ex:ax**2+bx+c   a must be 1')
                equation = input('enter the equation:')

                if equation[0] not in letters:
                    print('the equation (a) must be  1')
                

                elif int(equation[3]) != 2:
                    print('the equation must be second degree')

                
                else:
                    mes = find_suitable_factors(equation)
                    print(f'your solution is {mes}')
                    print(102*'=')
            
            elif choice == 2:
                print('THANK YOU')
                break 
        except ValueError:
            print('choose from the list ')
            print(102*'=')


if __name__ == '__main__':
    main()