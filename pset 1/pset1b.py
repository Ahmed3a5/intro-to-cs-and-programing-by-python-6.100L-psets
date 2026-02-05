#take the annual salary , percent to save , house cost from the user 

annual_salary = int(input('enter your yearly salary: '))
percent_to_save = float(input('enter the percent to save as deciml: '))
house_cost = int(input('enter the cost of your dream house: '))
semi_annual_raise = float(input('what is the semi annual raise as decimel: '))

# calculate the total cost he should save by add the down payment to house cost

down_payment = 0.25
total_cost = down_payment * house_cost

#calculate the monthly salary of the person 

month_salary = annual_salary / 12

#savings from salary monthly 

savings_from_salary = month_salary * percent_to_save

#iteration to calculate how many months to buy the house 

months = 0
# the N is the varible that iterate in the relation between months and increasee the salaray N == months *(1/6)because the salary inceases every 6 months 
N = 1
total_savings = 0
while total_savings < total_cost:
# calculate the total savings and increase the months  
    total_savings = savings_from_salary + (total_savings*(0.05/12)) + total_savings
    months +=1


# know if the Nmonths is equal to number of increase (N) multiple in the 6 the rate of increase and recalculate the savings and increas the N 
    if months == N*6:
#the new salary use updated so it will used when the loop start agian 
        month_salary = month_salary + (month_salary * semi_annual_raise)
        savings_from_salary = month_salary * percent_to_save
        N+=1


# print the months need for down pyment
print(f'NUmber of Months : {months}')