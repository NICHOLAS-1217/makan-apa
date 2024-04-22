from tkinter import *
from tkinter import messagebox
import tkinter.font
import pandas as pd
import random

# tkinter settings
def CenterWindowToDisplay(Screen: Tk, width: int, height: int):
    """Centers the window to the main display/monitor"""
    screen_width = Screen.winfo_screenwidth()
    screen_height = Screen.winfo_screenheight()
    x = int((screen_width/2) - (width/2))
    y = int((screen_height/2) - (height/1.5))
    return f"{width}x{height}+{x}+{y}"
root = tkinter.Tk()
photo = tkinter.PhotoImage(file = "makan_icon.png")
root.wm_iconphoto(False, photo)
root.title("Makan Apa ???")
root.geometry("500x455")
root.geometry(CenterWindowToDisplay(root, 900, 400)) 
h1 = tkinter.font.Font(family = "System",  size = 30)
h2 = tkinter.font.Font(family = "Courier New",  size = 20)  

# read files
read = open("RandomFood.txt", "r")
data = read.read()
df = pd.read_csv("restaurants_data_analysis.csv")

# intoduction
intro = tkinter.Label(root, text = "Makan Apa???")
intro.pack()
intro.configure(font = h1) 

# question 1
question1 = tkinter.Label(root, text = "Where are you?")
question1.pack()
question1.configure(font = h2)
location_input = StringVar()
location_input.set("Cyberjaya")
drop =  OptionMenu(root, location_input, 
                    "Cyberjaya", 
                    "Kuala Lumpur", 
                    "Kajang", 
                    "Bangi", 
                    "Petaling Jaya", 
                    "Subang", 
                    "Shah Alam", 
                    "Klang", 
                    "Putrajaya", 
                    "Sepang", 
                    "Rawang", 
                    "Ipoh", 
                    "Seri Iskandar", 
                    "Teluk Intan", 
                    "Kampar", 
                    "Kepala Bantas", 
                    "Kulim", 
                    "Sungai Petani",
                    "Alor Setar", 
                    "Jitra", 
                    "Arau", 
                    "Kangar",
                    "Kelantan",
                    "Terengganu",
                    "Kuantan", 
                    "Temerloh",
                    "Jerantut",
                    "Rompin",
                    "Negeri Sembilan",
                    "Port Dickson",
                    "Kuala Pilah",
                    "Bahau",
                    "Melaka",
                    "Johor Bahru",
                    "Pontian",
                    "Ulu Tiram",
                    "Kulai",
                    "Kota Tinggi",
                    "Kluang",
                    "Segamat",
                    "Tangkak",
                    "Mersing",
                    "Kuching",
                    "Petra Jaya",
                    "Samarahan",
                    "Sibu",
                    "Bintulu",
                    "Miri",
                    "Kota Kinabalu",
                    "Sandakan"
                    ).pack()

# question 2
question2 = tkinter.Label(root, text = "What is your budget?")
question2.pack()
question2.configure(font = h2)
budget_input = StringVar()
budget_input.set("low")
drop =  OptionMenu(root, budget_input, "low", "medium", "high").pack()

# submit part
def filter(location, cost):
    filtering = df[(df["city"] == location) & (df["budget"] == cost) & (df["vertical_parent"] == "Restaurant")]
    restaurants = filtering[["budget", "name", "city"]]
    restaurants_list = restaurants.values.tolist()
    answer = random.choice(restaurants_list)
    write = open("RandomFood.txt", "w")
    write.write(str(answer[1]))
    write.close()
    print(answer)
    result = tkinter.Label(root, text = str(answer[1]))
    result.pack()
    result.configure(font = h2)

counter = 0

def submit():
    global counter
    counter += 1
    if counter <= 3:
        location = location_input.get()
        budget = budget_input.get()
        cost = 0
        if budget == "low":
            cost = 1
        elif budget == "medium":
            cost = 2
        elif budget == "high":
            cost = 3
        filter(location = location, cost = cost)
    else:
        messagebox.showerror("showerror", "You are picky eater, no need to eat") 
        result = tkinter.Label(root, text = "You little picky eater, no need to eat")
        result.pack()
        result.configure(font = h1)
submit_button = tkinter.Button(root, text = "submit", command = submit)
submit_button.pack()
submit_button.configure(font = h2)

# end
root.mainloop()