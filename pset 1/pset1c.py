# take the inital deposit and define variables 
intial_deposit = int(input('enter your intial deposit: '))
epsilon = 100         # the epsiolon accepted is 100$ above or below the down payment
house_cost = 800000
down_payment = 0.25 * house_cost
high = 100               # the high range of r is 100%
low = 0                  # the low range of r is 0 %
r = (low+high)/2
steps = 0
max_savings = intial_deposit*(1+(float(100/100)/12))**36   # max savings when return r is 100 % is 


# evalute if the intial deposit exceed the down payment no need to calculate r = 0 
if intial_deposit > (down_payment - epsilon):
    r = 0
    steps = 0
elif max_savings < (down_payment - epsilon):
    r = None
    steps = 0
else:
    amount_saved = intial_deposit*(1+(float(r/100)/12))**36
    # iteration if the amount saved and down payment still above epsilon we remake the r range by bisection search 
    while abs(amount_saved - down_payment) >= epsilon:
        # make if the amount saved is above the down payment
        if amount_saved > down_payment:
            high = r         # reset the high rang for r if the amount saved is too high
        else:
            low = r     # reset the low rang for r if the amount saved is too low 
        steps +=1
        r = (low + high)/2       # re calculate the half of the high and low  == r 

        amount_saved = intial_deposit*(1+(float(r/100)/12))**36
        # evalute if we can not collect the down payment withen 36 months   

# priint the output according to the r have a value or not 
if r == None:
    print('best savings rate: ' , r)
    print('steps in bisection:', steps)
else:
    print('best savings rate: ' , float(r/100))
    print('steps in bisection search: ' , steps)
        

    
