import random, art

def game():
	print(art.logo)
	print("Welcome to the Number Guessing Game!")
	print("I'm thinking of a number between 1 and 100.")

	random_number = random.randint(1,100)
	level = input("Choose a difficulty. Type 'easy' or 'hard': ")

	if level.lower() == "easy":
		attempts = 10
	elif level.lower() == "hard":
		attempts = 5
	else:
		return "Invalid difficulty. Please try again."
	
	print(f"You have {attempts} attempts remaining to guess the number.")

	while attempts != 0:
		guess_number = int(input("Make a guess: "))
		if guess_number > random_number:
			attempts -= 1
			print(f"Too high.\nGuess again.\nYou have {attempts} attempts remaining to guess the number.")
		elif guess_number < random_number:
			attempts -= 1
			print(f"Too low.\nGuess again.\nYou have {attempts} attempts remaining to guess the number")
		elif guess_number == random_number:
			return f"You guess the right number. It was indeed {random_number}."
	
	return f"You've run out of guesses. The number was {random_number}.  bye bye." 

print(game())
