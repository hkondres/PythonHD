#!/usr/env python3

print("Welcome to twitter-handle app ")

# assigning variables for pet name and city of origin
petname = input("Write the name of your dead/alive/favorite pet: ")
city = input("Write the name of the city you were born: ")

# 2 different ways to get output
print("Your new twitter handle is " + "@cyber" + petname + " and you came from " + city)
print(f"Your new twitter handle is @cyber{petname} and you came from {city}")
