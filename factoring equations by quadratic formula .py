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



def extract_term_num(term):
    """
    """
    letters ='qwertyuioplkjhgfdsazxcvbnm'
    num = 0
    temp = ''
    for i in range(len(term)):
        if term[i] in letters:
            break
        else:
            temp += term[i]
    
    if temp == '+' or temp == '':
            num = 1
    elif temp == '-':
            num = -1
    else:
        num = int(temp)
    
    return num


def find_absolute_c(d , c):
    """
    """
    if d == 0:
        absolute_c = c
    else:
         absolute_c = c - d

    return absolute_c


def find_equation_terms(equation):
    temp = ''
    equation_terms = []
    for i in range(len(equation)):
        if equation[i] == '+':
            equation_terms.append(temp)
            temp = '+'
        elif equation[i] == '-':
            equation_terms.append(temp)
            temp = '-'
        else:
            temp += equation[i]
    final_equation_terms = []
    for term in equation_terms:
         if term != '':
              final_equation_terms.append(term)
    final_equation_terms.append(temp)
    
    return final_equation_terms

# equation = '-x**2+4x'
# print(find_equation_terms(equation))


def split_equation(equation):
    """
    equation is a second degreee mathematics eqation in a string form 
    retun a list of all three terms 
    """
    letters ='qwertyuioplkjhgfdsazxcvbnm'

    equation_parts = equation.split('=')

    d = int(equation_parts[1])


    if equation_parts[0][-1] in letters :
        c = 0
        equation_terms = find_equation_terms(equation_parts[0])
        a = extract_term_num(equation_terms[0])
        b = extract_term_num(equation_terms[1])

    elif equation_parts[0][-2] == '*':
         c = 0
         a = extract_term_num(equation_parts[0])
         b = 0

    
    else:
        equation_terms = find_equation_terms(equation_parts[0])

        if len(equation_terms) == 2:
            c = int(equation_terms[1])
            a = extract_term_num(equation_terms[0])
            b = 0
        
        elif len(equation_terms) == 3:
            c = int(equation_terms[2])
            a = extract_term_num(equation_terms[0])
            b = extract_term_num(equation_terms[1])

    absolute_c = find_absolute_c(d , c)     

    return a , b , absolute_c


# equation ='3x**2-8x=2'
# print(split_equation(equation))


def solve_equation(equation):
    """
    """
    a , b , c = split_equation(equation)

    under_root = (b**2) - (4*a*c) 

    if under_root < 0:
        complex_part = str(find_sqr_root(abs(under_root))/(2*a)) + 'i'
        real_part = str(-b /(2*a))

        first_solution = real_part + '+' + complex_part
        second_solution = real_part + '-' + complex_part

        return first_solution , second_solution
    
    else:

        first_solution = (-b + find_sqr_root((b**2 - (4*a*c)))) / (2*a)
        second_solution = (-b - find_sqr_root((b**2 - (4*a*c)))) / (2*a)

        return first_solution , second_solution



equation ='x**2+1=0'
print(solve_equation(equation))