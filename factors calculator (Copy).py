#==============================================================
########   A simple calculator for greatest common factor   ##########
# =============================================================

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




def split_numbers(numbers):
    """
        this is a function that take a string and return a list of integers in this string 
        string must be in the form of 1,2,3
    """
    ## the  list to append integers to 
    nums_list = []
    ## the temporary string that will hold the integers 
    temp = ''
    ## iterate through the string 
    for i in range(len(numbers)):
        ## if the char not equal to the , 
        if numbers[i] != ',':
            ## we concatenate the char to the temp 
            temp +=numbers[i]
        ## else we append the temp to list 
        ## and make the temp emptey again 
        else:
            if temp !='':
                nums_list.append(int(temp))
                temp =''
    if temp !='':
    ## we append the last integer in the string 
        nums_list.append(int(temp))
    return nums_list



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
            if temp not in factors:
                factors.append(temp)
                factors.append(i)

    return factors




def find_greatest(L):
    """ 
        this is a function take a list or dictionary L 
        retrun the greatest number in this data structure
    """
    ## we intialize the greatest number by 1 beacuse it is the greatest possible factor 
    greatest = 1
    ## if it is a lis 
    if type(L) == list:
        if len(L) == 0:
            return 0
        for i in range(len(L)):
            if L[i] >= greatest:
                greatest = L[i]
        
        return greatest
    ## if it is a dictionary 
    elif type(L) == dict:
        for k , v in L.items():
            if k >= greatest:
                greatest = k
    
        return greatest




def find_common_greatest_factor(x , y):
    """
        this function fin the greatest common factor for 2 numbers 
    """
    ## this is the empty list we append the factors at 
    common_factors = []
    ## we find the all factors of the x and y 
    x_factors = find_all_factors(x)
    y_factors = find_all_factors(y)
    ## we iterate through the 2 lists of all factors of x and y 
    ## and we find the common shared factors for the 2 numbers 
    for i in x_factors:
        for j in y_factors:
            if i == j:
                common_factors.append(i)
                break
    ## then after find the shared factors we find the greatest one 
    common_greatest_factor = find_greatest(common_factors)

    return common_greatest_factor




def modified_common_greatest_factor(args):
    """
        this function is modified from the old function to find a gcf for a list of numbers 
        args: is a list of numbers we need to find the gcf for it 
    """
    ## we make a list and dictionary and make the greatest varialbe by one 
    all_common_factors = []
    factors_dict = {}
    greatest = 1
    ## we iterate through the all numbers in the args and find all possible factors for each one and append it to the list 
    for arg in args:
        all_common_factors.extend(find_all_factors(arg))
    ## we iterate through the list to make the dictionary by how many times the factor occur
    ## dictionary {factor:how many times occure}
    ## how many times occur correspond the factor in which number the factor appear for example if appear in all numebers the occurance == len(args)
    ## 
    for i in all_common_factors:
        if i in factors_dict:
            factors_dict[i] +=1
        else:
            factors_dict[i] = 1
    ## then we find the greatest factor by iterate through the dictionary 
    ## if the factor occur in the all numbers this is the first conditoin 
    ## we see if the number is the greatest one or not
    for k , v in factors_dict.items():
        if  v == len(args):
            if k > greatest:
                greatest = k
    
    return greatest




def main():
    while True:
        ## the programe welcoing 
        print(102*'=')
        print(30*'=' , 'WELCOME TO SIMPLE GREATEST COMMON FACTOR' , 30*'=')
        print(102*'=')
        try:
            ## take the choice 
            print('1-Find the GCF')
            print('2-EXIT')
            choice = int(input())
            if choice == 1:
                try:
                    ## we take the input and calculate the GCF and print the result 
                    print('enter your numbers separated by comma without spacing EX(1,2)')
                    numbers = input()
                    nums_list = split_numbers(numbers)
                    gcf = modified_common_greatest_factor(nums_list)
                    print(f'your GCF is {gcf}')
                    ## if the input not as we expect 
                except ValueError:
                    print('INVALID INPUT')
                    print('TRY AGAIN')
            ## if the user want to exit
            elif choice == 2:
                print('THANK YOU')
                break
        ## if the choice as not we expect 
        except:
                print('INVALID CHOICE')
                print('TRY AGAIN')



if __name__ == '__main__':
    
    main()


    

