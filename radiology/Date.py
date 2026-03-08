class Date(object):
    """
        this is a class of date 
    """
    def __init__(self , day , month , year):
        self.day = day
        self.month = month
        self.year = year

        ## iterate if the user enter large days to generate 
        while self.day > self.get_monthlenght():  ## iteration if the self day still higher the month lenghth 
            ## if self day < monthe lenght break 

            self.day-=self.get_monthlenght()   ## return the month lenght and sustract it from the day 
            self.month+=1 ## increment the month 

        ## \\\\\\\\\\\\    the old logic \\\\\\\\\\\\\
        # ## logic if the month is 30 days only 
        #     if self.month in (11 ,9 ,6 ,4):
        #         if self.day > 30:              ## we reach the end of the month
        #             self.month +=1             ## increment the month
        #             self.day = self.day - 30   ## take the difference between the days above 31 and make it as days of new month

        #     ## if month is 2 which is 28 day
        #     elif self.month == 2:
        #         if self.day > 28:     ## same logic as above 
        #             self.month +=1
        #             self.day = self.day - 28
        #     ## if the month is 31 day 
        #     else:
        #         if self.day > 31:   ## same logic as above 
        #             self.month +=1     
        #             self.day = self.day - 31 
        #   

            ## we intialize the new year if the months > 12
            if self.month >12:
                self.year +=1
                self.month = self.month - 12

    
    def get_day(self):
        return self.day 
    
    def get_month(self):
        return self.month
    
    def get_year(self):
        return self.year
    
    ## make the date string like 
    def __str__(self):

        return str(self.day) + '/' + str(self.month) + '/' + str(self.year)
    
    ## make the equality check of the date and other date 
    def __eq__(self , other):

        if type(self) != type(other):
            return False
        elif self.day == other.day and self.month == other.month and self.year == other.year:
            return True 
        return False
        
    def get_monthlenght(self):
        if self.month in (11 ,9 ,6 ,4):
            return 30
        elif self.month == 2:
            return 28
        else:
            return 31 

        
    ## generate dates above the current date object 
    def generate_dates(self , num):
        """ this function return a list of dates from the num days we need to generate 

            num: is the number of days we generate it is the upper limit 
            self is the current date object
            
        """
        
        ## new list 
        dates = []
        ## we iterate through the object day till the day+number 
        for day in range(self.get_day() , self.get_day()+num+1 , 1):
            ## make a new date object of the day
            date = Date(day, self.get_month() , self.get_year() )
            # print(date)
            dates.append(date)
        
        ## return a list
        return dates

# date = Date(28 , 2 , 2026)
# dates = date.generate_dates(60)
# for date in dates:
#     print(date)


def convertdatestring(date):
    """
        this function take a date as string or object  and rturn a Date object of it or string of it 
        date is a srting of date formate 'day/month/year'
    """
    ## if the is an object type date we return the str of it 
    if type(date) == Date:
        return date.__str__()
    ## we split the string in the / to get each int alone 
    datestring = date.split('/')
    ## this is the new list to append intgers in it 
    dateinteger = []
    ## iterate through the date sting and convert each to int and append to list
    for i in datestring:
        i = int(i)
        dateinteger.append(i)
    ## make an object Date from the date integer list by indexing 
    date = Date(dateinteger[0] , dateinteger[1] , dateinteger[2])
    ## return the date object 
    return date


# date = '26/2/2026'
# date = convertdatestring(date)
# print(type(date))
# date = convertdatestring(date)
# print(type(date))



       
