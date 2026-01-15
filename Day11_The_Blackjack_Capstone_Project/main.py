import art
import random


def calculate_score(hand):
    """Calculate the best score for a given hand."""
    score = sum(hand)
    ace_count = hand.count(11)

    # Convert Ace from 11 to 1 if score is over 21
    while score > 21 and ace_count > 0:
        score -= 10
        ace_count -= 1

    return score


def blackjack():
    cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

    print(art.logo)
    print("Welcome to Blackjack!")

    # Initial hands
    your_hand = random.choices(cards, k=2)
    computer_hand = random.choices(cards, k=2)

    your_score = calculate_score(your_hand)
    computer_score = calculate_score(computer_hand)

    print(f"Your cards: {your_hand}, current score: {your_score}")
    print(f"Computer's first card: {computer_hand[0]}")

    # Player turn
    another_card = input("Type 'y' to get another card, type 'n' to pass: ")

    while another_card == "y":
        your_hand.append(random.choice(cards))
        your_score = calculate_score(your_hand)
        print(f"Your cards: {your_hand}, current score: {your_score}")

        if your_score > 21:
            break

        another_card = input("Type 'y' to get another card, type 'n' to pass: ")

    # Dealer turn
    if your_score <= 21:
        while computer_score < 17:
            computer_hand.append(random.choice(cards))
            computer_score = calculate_score(computer_hand)

    print(f"Your final hand: {your_hand}, final score: {your_score}")
    print(f"Computer's final hand: {computer_hand}, final score: {computer_score}")

    # Determine winner
    if your_score > 21:
        print("You went over 21. You lose.")
    elif computer_score > 21:
        print("Dealer went over 21. You win!")
    elif your_score > computer_score:
        print("You win!")
    elif your_score < computer_score:
        print("You lose.")
    else:
        print("Draw.")


# Game loop
continue_game = "y"

while continue_game == "y":
    print("\n" * 20)
    blackjack()
    continue_game = input("Do you want to play another round of Blackjack? Type 'y' or 'n': ")

print("Thank you for playing!")

