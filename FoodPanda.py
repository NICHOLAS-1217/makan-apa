import pandas as pd
import pyfiglet
import random

data = pd.read_csv("restaurants_data_analysis.csv")

def filter(location, cost):
    filtering = data[(data["city"] == location) & (data["budget"] == cost) & (data["vertical_parent"] == "Restaurant")]
    restaurants = filtering[["budget", "name", "city"]]
    restaurants_list = restaurants.values.tolist()
    answer = random.choice(restaurants_list)
    write = open("RandomFood.txt", "w")
    write.write(str(answer[1]))
    write.close()
    print(answer)
    result = pyfiglet.figlet_format(answer[1])
    print(result)