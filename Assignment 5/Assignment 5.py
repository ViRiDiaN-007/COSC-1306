#assignment 5

import random as r
secret = r.randint(0, 100)

correct = False
numGuesses=0
lowerBound = 0
upperBound = 100

while not correct:
    print('Range of secret number is between ['+str(lowerBound)+','+str(upperBound)+']')
    try:
        guess = int(input('Enter your guess: '))
    except ValueError:
        print("That's not a number! Try again.\n")
    else:
        numGuesses +=1
        if guess > 100:
            print('Take a step back! The number is between [0,100]')
    
        elif guess == secret:
            print('You guessed it!')
            print('It took you ' + str(numGuesses)+ ' guesses')
            correct = True
            break
        elif guess < secret:
            print('Your guess is too low. Try again!\n ')
            lowerBound = int(guess)+1
        else:
            print('Your guess is too high. Try again!\n ')
            upperBound = int(guess)-1
input()
