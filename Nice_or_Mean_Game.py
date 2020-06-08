"""

Python:     3.8

Author:     Troy D. Boren

Purpose:    The Tech Academy - Python Course, creating our first program together.
            Demonstrtating how to pass variablews from funtion to function
            while producing a functional game.

            Remember, function_name(variable) _means that we pass the variable.
            return variable _means that we are returning the variable to
            back to the calling function.
            
"""

def start(nice=0,mean=0,name=""):
    # get user's name
    name = describe_game(name)
    nice,mean,name = nice_mean(nice,mean,name)

def describe_game(name):
    """
        Check if this is a new game or not.
        If it is a new game, get the user's name.
        If it is not a new game, thank the player for
        playing again and continue with the game.
        
    """
    
    # meaning, if we do not already have this user's name,
    # then they are a new player and we need to get their name.
    
    if name != "":
        print("\n Thank you for playing again, {}!".format(name))
        
    else:
        stop = True
        while stop:
            if name == "":
                name = input("\n What is your name? \n >>> ").capitalize()
                if name != "":
                    print("\n Welcome, {}!".format(name))
                    print("\n In this game, you will be greeted \n by several different people. \n You can choose to be nice or mean,")
                    print(" but at the end of the game your fate \n will be sealed by your actions.")
                    stop = False
    return name

def nice_mean(nice,mean,name):
    stop = True
    while stop:
        show_score(nice,mean,name)
        pick = input("\n A stranger approaches you for a \n conversation. Will you be nice \n or mean? (N/M) \n >>>: ").lower()
        if pick == "n":
            print("\n The stranger walks away smiling...")
            nice = (nice + 1)
            stop = False
        if pick == "m":
            print ("\n The stranger glares at you \n menacingly and storms off...")
            mean = (mean + 1)
            stop = False
    score(nice,mean,name) # pass the 3 variables to the score().

def show_score(nice,mean,name):
    print("\n {}, your current total: \n ({}, Nice) and ({}, Mean)".format(name, nice, mean))

def score(nice,mean,name):
    # score function is being passed the values stored within the 3 variables
    if nice > 2: # if condition is valid, call win function passing in the variables so it can use them
        win(nice,mean,name)
    if mean > 2: # if condition is valid, call lose function passing in the variables so it can use them
        lose(nice,mean,name)
    else:        # else, call nice_mean function passing in the variables so it can use them
        nice_mean(nice,mean,name)

def win(nice,mean,name):
    # Substitute the {} wildcards with our variable values.
    print("\n Nice job {}, you win! \n Everyone loves you and you've \n made lots of friends along the way!".format(name))
    # call again function and pass in our variables
    again(nice,mean,name)

def lose(nice,mean,name):
    #Substitute the {} wildcards with our variable values.
    print("\n Ahhh too bad, game over! \n, You live in a dirty beat-up \n van down by the river, wretched and alone!".format(name))
    # call again function and pass in our variables
    again(nice,mean,name)

def again(nice,mean,name):
    stop = True
    while stop:
        choice = input("\n Do you want to play again? (y/n): \n >>> ").lower()
        if choice == "y":
            stop = False
            reset(nice,mean,name)
        if choice == "n":
            print("\n Oh, so sad, sorry to see you go!")
            stop = False
            quit()
        else:
            print("\n Enter ( Y ) for 'YES', ( N ) for 'NO': \n >>> ")

def reset(nice,mean,name):
    nice = 0
    mean = 0
    # Notice, I do not reset the name variable as that same user has elected to play again.
    start(nice,mean,name)

if __name__ == "__main__":
    start()
