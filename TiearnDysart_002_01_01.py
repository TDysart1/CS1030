#Convert a height to meters 
#prompt user to input height in feet and inches
# userFt = int(input('What is you height in feet? '))
# userIn = int(input('In inches? '))
# userSumIn = (((userFt) * 12) + userIn)   
#users inputs are then gathered as int values to be converted to intches total 


userFt = (input('What is your height in feet? ')) #ask user to input height in feet
try: #try/except was used to make sure that if the input is 
#anything but an integer it will throw error
    userFt == int(userFt)
except ValueError:
    print('Not a number value!')
    raise SystemExit


userIn = (input('Any inches? '))
try: #Same try/except for the inches input that was used for the feet
    userFt == int(userFt) and userFt == int(userFt)
    #creating the variable that int values of feet and inches are then 
#turned into the sum of inches. Feet times 12 + whatever inches where added 
    userSumIn = ((int(userFt) * 12) + int(userIn))
except ValueError:
    print('Not a number value!')
    raise SystemExit



    

#functon doing the formula to return the 
# vaule of users summed inches(userSumIn) and turns into userM(eters)
def heightMeters (userSumIn):
    userCm = int(userSumIn * 2.54)
    userM = userCm / 100
    return userM
        #FUNCTION THAT CONVERTS ALL VALUES INTO METERS ^^^


#not to convert it all into a string to make a sentence
# takes the userSumIn as the value...        
def convert_to_string(userSumIn):
    if userSumIn > 0 and userSumIn <= 95: #if the value is between 0 and 95         
        fT = str(userFt) #convert userFt to a string
        iN = str(userIn) #conver userIn to a string
        mM = str(round(heightMeters(userSumIn),2)) #taking the heightMeters value we 
        #use round to take the value to 2 decimals places.
        print('Original height is ' + fT + ' feet and ' + iN + ' inches. That converts to ' + mM + ' meters tall!')
        #our sentence will return all values properly spaced                
    else: 
        print ('you are really tall!') 
        #prints the statement if you are just tall 

convert_to_string(userSumIn)
#calls are function so we can print our sentences 

    
    
   
    #WHILE THE VAULES REMAIN  WILL BREAK 
