#!/usr/bin/python3

guess = int(input("Enter the age : "))

if guess > 10 and guess < 20:
    print("In range")
elif guess > 50:
    print("Too Old")
else:
    print("Out of range")

