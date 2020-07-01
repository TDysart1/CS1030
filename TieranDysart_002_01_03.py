#Write a program that reads a position from the user. Use an if statement to determine 
#if the column begins with a black square or a white square. Then use modular
#arithmetic to report the color of the square in that row. For example, 
#if the user enters a1 then your program should report that the square is black. 
#If the user enters d5 then your program should report that the square is white. 
#Program with print an error message and exit if you input values that can't be used  
#User input requires a space to get both values 
#The table we are using all the even letters b,d,f,h are black squares 
#when the even numbers are the picked with the even letter
#The odd table a,c,e,g are black squares when the numbers are odd 
#so d and any even number 2,4,6,8 will result black 
#d and odd number will result in white 

board_values = ['a','b','c','d','e','f','g','h'] # a list of all letter values 
even_board = ['b','d','f','h'] # the even letters 
odd_board =['a','c','e','g'] #the odd letters

#user input value A-H and value 1-8 
board_row,board_col = input('Please input a letter a-h and a number 1-8. Put a space between inputs ').split()
# takes to variables and assigns them based on users input. Letter first than number
# don't do a letter first it will throw error
user_letter = str(board_row) #this throws error cause looking for a string in the first input
user_num = int(board_col) #looking for a number value in the second input 

def checker_board(user_letter,user_num): #function takes user inputs as arguements 
    #if statement checks the odd board list to see if users input is in that list
    if board_row in odd_board:
        #if found than moves on to the number, checks if number cant be divided by 2 
        if user_num % 2 != 0:
            print(board_row+board_col,'is a black square')      
        else: # if the number is divisble by 2 then the square will be white 
            print(board_row+board_col,'is white square')
    else: #the else is here if the letter the user inputs is in not in the odd_board 
        if user_num % 2 == 0: # number is divisble by 2 result black
            print(board_row+board_col,'is a black square ')
        else: #else result white 
            print(board_row+board_col,'is a white square')



#if statement checks if the user input values are in board values and between 1-8 
# if not print error and exit
if user_letter in board_values:
    if user_num < 1 or user_num > 8:
        print('That is not a valid number!')
        exit 
    else:
        checker_board(user_letter,user_num)
else:
    print('Incorrect input!')
    exit

