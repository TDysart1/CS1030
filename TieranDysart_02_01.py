#Compute a Grade point average 
# A+/4.2 A/4.0 A-/3.9 B+/3.7 B/3.2 
# B-/3.0 C+/2.8 C-/2.0 D+/1.8 D/1.2 F/0

#create a list of letter grades
letter_grades = ['A+','A','A-','B+','B','B-','C+','C','C-','D+','D','F']
number_of_grades = int(input('How many grades are you putting in 1-7?'))
input_counter = 0
user_grades = []

while True:
    grades_submitted = input(str('Input your letter grades press Q to exit: '))
    #prompt user to do letter grades
    if (grades_submitted in letter_grades):
        user_grades.append(grades_submitted)
        input_counter = input_counter + 1
        if (input_counter == int(number_of_grades)):
            break
            
       
        
#convert that list to a GPA
def grades_to_Gpa (user_grades):
#calculates overall GPA for letter grades entered
    score_range = {'A+':4.2,'A':4.0,'A-':3.9,'B+':3.7,'B':3.2,'B-':3.0,'C+':2.8,'C':2.2,'C-':2.0,'D+':1.8,'D':1.2,'F':0}
    total = 0 
    for grades_submitted in user_grades:
        total += score_range[grades_submitted]
    print (sum(score_range[grades_submitted]for grades_submitted in user_grades)/number_of_grades)    
       
        
grades_to_Gpa(user_grades)
