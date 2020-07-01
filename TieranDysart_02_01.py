#Compute a Grade point average 
# A+/4.2 A/4.0 A-/3.9 B+/3.7 B/3.2 
# B-/3.0 C+/2.8 C-/2.0 D+/1.8 D/1.2 F/0

#create a list of letter grades, then ask user to input grades one at a time 
letter_grades = ['A+','A','A-','B+','B','B-','C+','C','C-','D+','D','F']
number_of_grades = int(input('How many grades are you putting in 1-7?'))
input_counter = 0 #how many grades want to be entered 
user_grades = []

while True:
    grades_submitted = input(str('Input your letter grades press Q to exit: '))
    #prompt user to do letter grades
    if (grades_submitted in letter_grades):
        user_grades.append(grades_submitted)
        input_counter = input_counter + 1
        if (input_counter == int(number_of_grades)):
            break
    #while loop will continue to add the grades to the list until we reach the number of grades reqiured 
       
        
#convert that list to a GPA
def grades_to_Gpa (user_grades):
#calculates overall GPA for letter grades entered, created a dictionary storing the letter grade and it GPA value
    score_range = {'A+':4.2,'A':4.0,'A-':3.9,'B+':3.7,'B':3.2,'B-':3.0,'C+':2.8,'C':2.2,'C-':2.0,'D+':1.8,'D':1.2,'F':0}
    total = 0 
    #loop through grades submitted and I add the values of each grade to the total
    for grades_submitted in user_grades:
        total += score_range[grades_submitted] #add the values that equal the same values in grades submitted and values
        #from score range 
    print (sum(score_range[grades_submitted]for grades_submitted in user_grades)/number_of_grades)    
       #this will take that total and divide it by number of grades
        
grades_to_Gpa(user_grades)
