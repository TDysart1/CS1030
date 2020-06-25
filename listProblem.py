#Problem 1

mylist =[] #list variable 
while True: #continue running loop as long as number choice is greater than 0 
    numberChoice = input("Enter a value greater than 0: ")#ask user input 
    mylist.append(numberChoice)#adds the new input into the list 
    if int(numberChoice) <= 0 : #check if input entered is less than or equal to zero
        print("NUMBER LESS THAN ZERO: ") #fires off when number is less than or equal to 0
        print(mylist) #prints current list with negative number 
        break
    
    print(mylist)