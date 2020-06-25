
#Leap Year Assignment 
# user inputs year and runs it against the function 
year = int(input('Enter a year to see if that year is a leap year: '))
 
#function that checks the year entered and whether it is a leap year 
def leapYear(year):
        if (year % 4) == 0: # checks if year is even divided by 4/100/400 
            if (year % 100) == 0:
                if (year % 400) == 0:
                    return True
                else: #not divisable by 400 
                    return False
            else: #divisable by 4 and 100 but not 400 is still a leap year.          
                return True
        else: #if not divisable by 4 than not a leap year
            return False

#function statements checks to see if it returns true or false and prints the correct statement
# if the year is greater or equal to 1582 than proceed with statements else say print the else  
def statements():
    leapYear(year)
    if (year >= 1582):
        if True:
            print(year,'is a leap year.')
        else:
            print(year,'is not a leap year.')
    else:
        print('Year is before the time leap year was implemented !')
        
statements() #call the function 
