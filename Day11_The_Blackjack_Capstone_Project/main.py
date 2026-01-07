import art, random
#assuming that each card has the same probability
#jack/queen/king are 10
#ace can count as 11 or 1. We sent it as 11 until the user goes over 21. Switches to 1.
#cards are not removed
cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

print(art.logo)
print("Welcome to Blackjack!")
print("Dealer passes you two cards")

#randomly picked two cards for the player
your_hand = random.choices(cards, k=2)
computer_hand = random.choice(cards) #randomly picks one card for the dealer
#variables to hold the sum of the cards for the player and dealer
your_score = 0 
computer_score = 0

#loops through the list of numbers and sums it up
for card in your_hand:
    your_score += card

print(f"Your cards: {your_hand}, current score: {your_score}")
print(f"Computer's first card: {computer_hand}")

another_card = input("Type 'y' to get another card, type 'n' to pass: ")
