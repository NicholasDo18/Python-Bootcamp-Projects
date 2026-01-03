import art
print(art.logo)

#create functions for adding, subtracting, multiplying, and dividing
def add(n1, n2):
    return n1 + n2

def sub(n1, n2):
    return n1 - n2

def mul(n1, n2):
    return n1 * n2

def div(n1, n2):
    return n1 / n2

final_result = 0 #variable to hold all the calculations

n1 = float(input("What's the first number?: "))
operation = input("+\n-\n*\n/\nPick an operation: ")
n2 = float(input("What's the second number?: "))

if operation == "+":
    final_result = add(n1, n2)
    print(f"{n1} + {n2} = {add(n1, n2)}")
elif operation == "-":
    final_result = sub(n1, n2)
    print(f"{n1} - {n2} = {sub(n1, n2)}")
elif operation == "*":
    final_result = mul(n1, n2)
    print(f"{n1} * {n2} = {mul(n1, n2)}")
else:
    final_result = div(n1, n2)
    print(f"{n1} / {n2} = {div(n1, n2)}")

loopy = True

while loopy:
    continue_calculator = input(f"Type 'y' to continue with {final_result}, or type 'n' to start a new calculation: ").lower()

    if continue_calculator == "y":
        operation = input("+\n-\n*\n/\nPick an operation: ")
        n3 = float(input("What's the next number?: "))
        if operation == "+":
            print(f"{final_result} + {n3} = {add(final_result, n3)}")
            final_result = add(final_result, n3)
        elif operation == "-":
            print(f"{final_result} - {n3} = {sub(final_result, n3)}")
            final_result = sub(final_result, n3)
        elif operation == "*":
            print(f"{final_result} * {n3} = {mul(final_result, n3)}")
            final_result = mul(final_result, n3)
        else:
            print(f"{final_result} / {n3} = {div(final_result, n3)}")
            final_result = div(final_result, n3)
    else:
        loopy = False
        exit()

