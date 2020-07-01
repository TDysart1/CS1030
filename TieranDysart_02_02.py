from random import randint

#create a function that runs heads and tails coin flip.
#simulation is how many times I want to flip coins. IE 3 would mean I
# run the program 3 times each giving different results

def coin_flip():
    user_input = input('How many simulations? ')
    user_sim = int(user_input)
    coin_streak = 3 #highest amount of consectutive results
    results = []#open array to save the results of what was flipped
    flips_numbers = []#storing the flip totals of each simulation
    total_flips = 0 #keeps track of total flips
    sim_counter  = 0 #keeps track of user request
    head_counter = 0 #how many times head shows up 
    tails_counter = 0 #how many times tails shows up
    while sim_counter != user_sim:
        #while statement saying as long a the simulations counter isnt equal to user
        #input on how many simulations keep running the test
        if user_input == '' or user_sim <= 0:
            print('Invalid input!')
            exit()
        #^^^ if statement checks to see if the input is a correct input
        total_flips += 1 #total
        side = flip_side() #sets function flip_side() to variable 
        results.append(side)#adding flip result to the array 

        #if statement that checks side of coin
        if side == 'H':
            head_counter += 1
            # add one to the counter
            if head_counter == coin_streak:
                sim_flips = len(results)
                flips_numbers.append(sim_flips)
                print('_________')
                print('3 heads in a row, took',sim_flips,'flips!')
                print(results)
                sim_flips = 0 
                results.clear()
                sim_counter += 1
            #if statement checks the value of head counter and if it equals the streak
            # set the number of flips it took to sim_flips and then append that to the 
            # list of flip totals printing the results and how many flips it took
            # sets the simulated flips back to zero clears the results and updates
            # the counter of simulations. else setting tails to zero because we are 
            # looking for the heads to be consecutive so we have to make sure tails counter
            # resets to zero. If not wont be able to catch 3 in a row      
            else:
                tails_counter = 0 

             #if statement for the tails results same as heads if    
        else:
            tails_counter += 1
            if tails_counter == coin_streak:
                sim_flips = len(results)
                flips_numbers.append(sim_flips)
                print('_________')
                print('3 tails in a row took',sim_flips,'flips!')  
                print(results)
                sim_flips = 0 
                results.clear()
                sim_counter += 1  
            else:
                head_counter = 0 
    #final else statement prints all the results. Use max on the flip numbers array
    #to get the highest number of flips and min for the minimum
    #dividing total flips by how many simulations gets us the average
    #printing the last statement of how many total flips it took 
    else:
        print('_________')
        print('The max number of flips:',max(flips_numbers))
        print('The min number of flips:',min(flips_numbers))
        print('The average number of flips:',((total_flips/user_sim)))
        print('Total number of flips',total_flips)
   


#flip coin function that randomly chooses 1 - Heads or 2 - tails returning that value 
def flip_side():
    
    random_choice = randint(1,2)
    if random_choice == 1:
        coin_side = 'H'
    else:
        coin_side = 'T'
    
    return coin_side
    
coin_flip()
