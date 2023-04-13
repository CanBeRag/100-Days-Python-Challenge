
names_string = input("Give me everybody's names, separated by a comma. ")
names = names_string.split(", ")


import random

number_of_people = len(names)

random_people = random.randint(0, number_of_people - 1)
payee = names[random_people]

print(f"{payee} is going to buy the meal today!")
