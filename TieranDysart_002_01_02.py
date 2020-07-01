#convert miles per gallon to kilometers per liter 

#user inputs miles 
user_miles = float(input('please input a number of miles: '))

#inputs gallons 
user_gallons = float(input('please input a number of gallons: '))


def howMuch(user_miles,user_gallons):
#any value  <= 0 exit program 
    if user_miles <= 0 or user_gallons <= 0:
        exit
    else:
#convert miles to kilometer 1 mile = 1.6 km
        user_km = user_miles * 1.64
        user_mpg = round(user_miles / user_gallons, 1)
#convert gallons to liters 1 gallon to 3.785 liters
        user_liters = user_gallons * 3.785
        user_kml = round((user_km / user_liters),1)
        print('Your car gets',user_mpg, 'miles per gallon. Thats', user_kml,'kilometers per liter!')
#print our sentence giving us miles per gallon and kilometers per liter
#calling the function with the inputs

howMuch(user_miles,user_gallons)