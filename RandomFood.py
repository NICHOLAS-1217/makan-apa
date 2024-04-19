import random
import pyfiglet

read = open("RandomFood.txt", "r")
data = read.read()

low_cost_list = ["Hinz", "Face To Face", "Mama Homecook", "Mcdonalds"]
medium_cost_list = ["Kung Fu", "Taco Bell", "Texas"]
high_cost_list = ["Uncle Dons", "A&W", "Domino's Pizza", "4 Fingers"]
all_list = [low_cost_list, medium_cost_list, high_cost_list]

def random_choice(choice):
    answer = ""
    if choice == "low":
        answer += random.choice(low_cost_list)
    elif choice == "medium":
        answer += random.choice(medium_cost_list)
    elif choice == "high":
        answer += random.choice(high_cost_list)
    write = open("RandomFood.txt", "w")
    write.write(answer)
    write.close()
    ascii_answer = pyfiglet.figlet_format(answer)
    print(ascii_answer)

ascii_art = pyfiglet.figlet_format("Makan Apa ???")
print(ascii_art)
print(f"Your last chosen restaurant was: {data}")
choice = input("What cost would you wanna choose? (low, medium, high)\n").lower()

if data in low_cost_list:
    low_cost_list.remove(data)
    random_choice(choice = choice)
    low_cost_list.append(data)
elif data in medium_cost_list:
    medium_cost_list.remove(data)
    random_choice(choice = choice)
    medium_cost_list.append(data)
elif data in high_cost_list:
    high_cost_list.remove(data)
    random_choice(choice = choice)
    high_cost_list.append(data)









