import art
print(art.logo)
print("Welcome to the secret action program.\nHIGHEST BID GETS AN INTERNSHIP!!!")

bid_dict = {}

name = input("What is your name?: ")
bid = int(input("What's your bid?: $"))
bid_dict[name] = bid
any_bidders = input("Are there any other bidders? Type \'yes\' or \'no\'.\n ")

print(bid_dict[name])
while any_bidders == 'yes':
    print("\n" * 20)
    name = input("What is your name?: ")
    bid = float(input("What's your bid?: $"))
    bid_dict[name] = bid
    any_bidders = input("Are there any other bidders? Type \'yes\' or \'no\'.\n ")

highest_bid = max(bid_dict, key=bid_dict.get)
print("\n" * 20)
print(f"the winner is {highest_bid} with a bid of ${bid_dict[highest_bid]}.")
