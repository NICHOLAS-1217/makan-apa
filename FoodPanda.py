import pandas as pd
import random

data = pd.read_csv("restaurants_data_analysis.csv")
print(data)

# location input
location = input("What city are you at?\n").lower()
location = location[0].upper() + location[1:]

# cost input
budget = input("how much budget would you like?\n").lower()

cost = 0
if budget == "low":
    cost = 1
elif budget == "medium":
    cost = 2
elif budget == "high":
    cost = 3

def filter(location, cost):
    filtering = data[(data["city"] == location) & (data["budget"] == cost) & (data["vertical_parent"] == "Restaurant")]
    restaurants = filtering[["budget", "name", "city"]]
    restaurants_list = restaurants.values.tolist()
    print(random.choice(restaurants_list[1]))
filter(location = location, cost = cost)