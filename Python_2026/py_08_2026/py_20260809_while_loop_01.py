#!/usr/bin/python3

correctNumber = 5
guess = 0
while guess != correctNumber:
    guess = int(input("Guess the number: "))
    
    if guess != correctNumber:
        print('False guess')

print('You guessed the correct number')

