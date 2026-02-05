#take the annual salary , percent to save , house cost from the user 

annual_salary = int(input('enter your yearly salary: '))
percent_to_save = float(input('enter the percent to save as deciml: '))
house_cost = int(input('enter the cost of your dream house: '))

# calculate the total cost he should save by add the down payment to house cost

down_payment = 0.25
total_cost = down_payment * house_cost

#calculate the monthly salary of the person 

month_salary = annual_salary / 12

#savings from salary monthly 

savings_from_salary = month_salary * percent_to_save

#iteration to calculate how many months to buy the house 

N = 0
total_savings = 0
while total_savings < total_cost:
    total_savings = savings_from_salary + (total_savings*(0.05/12)) + total_savings
    N +=1
print(f'NUmber of Months : {N}')