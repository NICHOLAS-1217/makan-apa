import pyfiglet
from FoodPanda import filter

# read text file
read = open("RandomFood.txt", "r")
data = read.read()

# introduction
intro = pyfiglet.figlet_format("Makan Apa ???")
print(intro)
print(f"Your last chosen restaurant was: {data}")

# inputs
location = input("What city are you at?\n").lower()
location = location[0].upper() + location[1:]
budget = input("What cost would you wanna choose? (low, medium, high)\n").lower()

cost = 0
if budget == "low":
    cost = 1
elif budget == "medium":
    cost = 2
elif budget == "high":
    cost = 3

filter(location = location, cost = cost)

is_good = False

try_time = 0

while is_good == False:
    result = input("Is this good for you? (y/n)\n")
    if result == "n":
        filter(location = location, cost = cost)
        is_good = False
        try_time += 1
        if try_time > 3:
            print(pyfiglet.figlet_format("You are picky eater, no need to eat"))
            is_good = True
            break
    else:
        print("let's goooo!!!")
        is_good = True
        break








