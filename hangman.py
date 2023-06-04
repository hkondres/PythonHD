# create a greeting
# create your wordlist
# randomly choose a word from the list you have created
# ask the user to guess a letter
# bonus - let the program take the input from the user
# check if the letter is in the word
# import random
#
# # List of words to choose from
# words = ["apple", "banana", "cherry", "orange", "pineapple"]
#
# # Choose a random word from the list
# chosen_word = random.choice(words)
#
# # Ask the user to guess the letter position
# letter_position = int(input(f"Guess the position of a letter in the word '{chosen_word}': "))
#
# # Get the letter at the chosen position
# letter = chosen_word[letter_position - 1]
#
# # Print the letter and its position in the word
# print(f"The letter '{letter}' is at position {letter_position} in the word '{chosen_word}'.")
 

import random

# Ask the user to input a list of words
words = input("Enter a list of words separated by commas: ").split(",")

# Choose a random word from the list
chosen_word = random.choice(words)

# Ask the user to guess the letter position
letter_position = int(input(f"Pick the position of a letter in the word '{chosen_word}' and I will tell you which letter it is : "))

# Get the letter at the chosen position
letter = chosen_word[letter_position - 1]

# Print the letter and its position in the word
print(f"The letter '{letter}' is at position {letter_position} in the word '{chosen_word}'.")

