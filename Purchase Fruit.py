prices = {apple: 1.18, banana: 0.58, orange: 1.33}

fruit = [apple, banana, orange]

food = input("What is your food?: ")

if food == "apple":
    budget = float(input("That will be $" + str(price[0]) + ": "))
    if budget > apple:
        print(f"{'Thank you, your change is $'} {round(budget - apple, 2)}")
    if budget < apple:
        print(f"{'I am sorry, you still owe $'} {round(apple - budget, 2)}")
    if budget == apple:
        print("Thank you")

if food == "banana":
    budget = float(input("That will be $" + str(price[1]) + ": "))
    if budget > banana:
        print(f"{'Thank you, your change is $'} {round(budget - banana, 2)}")
    if budget < banana:
        print(f"{'I am sorry, you still owe $'} {round(banana - budget, 2)}")
    if budget == banana:
        print("Thank you")


if food == "orange":
    budget = float(input("That will be $" + str(price[2]) + ": "))
    if budget > orange:
        print(f"{'Thank you, your change is $'} {round(budget - orange, 2)}")
    if budget < orange:
        print(f"{'I am sorry, you still owe $'} {round(orange - budget, 2)}")
    if budget == orange:
        print("Thank you")
