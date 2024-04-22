import pyfiglet
import pandas as pd
import random

# read text file
read = open("RandomFood.txt", "r")
data = read.read()
df = pd.read_csv("restaurants_data_analysis.csv")

def filter(location, cost):
    filtering = df[(df["city"] == location) & (df["budget"] == cost) & (df["vertical_parent"] == "Restaurant")]
    restaurants = filtering[["budget", "name", "city"]]
    restaurants_list = restaurants.values.tolist()
    answer = random.choice(restaurants_list)
    write = open("RandomFood.txt", "w")
    write.write(str(answer[1]))
    write.close()
    print(answer)
    result = pyfiglet.figlet_format(answer[1])
    print(result)

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
        if try_time > 2:
            print("##########################################################################")
            print(pyfiglet.figlet_format("You are picky eater, no need to eat"))
            is_good = True
            break
    else:
        print("##########################################################")
        print(pyfiglet.figlet_format("let's goooo!!!"))
        is_good = True
        break








