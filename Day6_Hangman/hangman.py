import random
word_list = ["aardvark", "baboon", "camel"]

chosen_word = random.choice(word_list)
print(chosen_word)

# TODO-1: Create a "placeholder" with the same number of blanks as the chosen_word
placeholder = ""
for character in chosen_word: #adds blank lines for each character for our chosen word
    placeholder += "_"

print(placeholder)
guess = input("Guess a letter: ").lower()

# TODO-2: Create a "display" that puts the guess letter in the right positions and _ in the rest of the string.
display = ""
for letter in chosen_word: #This loops through each letter in the chosen word
    if guess == letter: #If our guess was correct, it would be added to the display
        display += letter
    else: #otherwise, it just adds a blank if we didn't guess right
        display += "_"

print(display)
