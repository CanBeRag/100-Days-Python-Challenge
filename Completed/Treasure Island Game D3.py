print('''
*******************************************************************************
          |                   |                  |                     |
 _________|________________.=""_;=.______________|_____________________|_______
|                   |  ,-"_,=""     `"=.|                  |
|___________________|__"=._o`"-._        `"=.______________|___________________
          |                `"=._o`"=._      _`"=._                     |
 _________|_____________________:=._o "=._."_.-="'"=.__________________|_______
|                   |    __.--" , ; `"=._o." ,-"""-._ ".   |
|___________________|_._"  ,. .` ` `` ,  `"-._"-._   ". '__|___________________
          |           |o`"=._` , "` `; .". ,  "-._"-._; ;              |
 _________|___________| ;`-.o`"=._; ." ` '`."\` . "-._ /_______________|_______
|                   | |o;    `"-.o`"=._``  '` " ,__.--o;   |
|___________________|_| ;     (#) `-.o `"=.`_.--"_o.-; ;___|___________________
____/______/______/___|o;._    "      `".o|o_.--"    ;o;____/______/______/____
/______/______/______/_"=._o--._        ; | ;        ; ;/______/______/______/_
____/______/______/______/__"=._o--._   ;o|o;     _._;o;____/______/______/____
/______/______/______/______/____"=._o._; | ;_.--"o.--"_/______/______/______/_
____/______/______/______/______/_____"=.o|o_.--""___/______/______/______/____
/______/______/______/______/______/______/______/______/______/______/_____ /
*******************************************************************************
''')
print("Welcome to Treasure Island.")
print("Your mission is to find the treasure.") 


road = input("You find yourself in a deserted road, a tree has fallen due to a storm and you can only go left or right. Where do you go? Left or Right? \n ")
road = f"{road}".lower()

if road == "right":
  print("You go right and suddenly due to the storm you lose sight of the way and fall into a ravine.")
  print("Game Over~")

else:
  wait = input("You keep going left and find a huge ocean and a deserted beach, You have two options either to swim or wait. Swim / wait? \n ")
  wait = f"{wait}".lower()
  if wait == "swim":
    print('''You start swimming in the deep black ocean and suddenly see a group of sharks swifting towards you! You try to swim back to the shore but it was too late... ''' )
    print("Game Over~")
    
  elif wait == "wait":
    print('''You go beside a rock and wait for someone to arrive, after a while you see a boat approaching and you start shouting for 
    help. Thankfully the guy with the boat hears you and picks you up from the deserted place... ''')
    print('''You tell him the island you want to go to and him with a scary face says asks you if you're sure about that? He tells you 
    really scary stories about people who went there and never returned~ ''')
    print("You with a scary heart tells him to take you there anyway... ")

  doors = input('''You arrive at the island and see three doors, Red, Blue and Yellow. Which door are you choosing? R / Y / B ? ''')
  doors = f"{doors}".lower()

  if doors == "r":
    print("You go into the red door and see fire all over the place!... ")
    print("Game Over~")

  elif doors == "y":
    print("You choose the yellow door and find yourself in a great beach and finally get saved!")
    print("You win!")

  else:
    print("You walk into the blue door and find yourself in a room full of piranas and sharks!")
    print("Game Over~")

    

