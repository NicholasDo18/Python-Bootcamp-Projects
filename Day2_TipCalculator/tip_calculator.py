print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
percentage = int(input("How much tip would you like to give? 10, 12, or 15?  "))
split_bill = int(input("How many people to split the bill? "))
percentage_tip = percentage / 100
tip = percentage_tip * total_bill
total_bill += tip
total_bill /= split_bill
total_bill = round(total_bill, 2)
print("Each person should pay: " + "$" + str(total_bill))

