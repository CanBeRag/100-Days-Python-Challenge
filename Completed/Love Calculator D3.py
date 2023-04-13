# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇

combine = name1 + name2 
combine_lower = combine.lower()

t = combine_lower.count('t')
r = combine_lower.count('r')
u = combine_lower.count('u')
e = combine_lower.count('e')
true = t + r + u + e

l = combine_lower.count('l')
o = combine_lower.count('o')
v = combine_lower.count('v')
e = combine_lower.count('e')
love = l + o + v + e

result = int(str(true) + str(love))

if (result <= 10) or (result >= 90):
    print(f"Your score is {result}, you go together like coke and mentos.")
elif result >= 40 and result <= 50:
    print(f"Your score is {result}, you are alright together.")
else:
    print(f"Your score is {result}.")