#If the bill was $150.00, split between 5 people, with 12% tip. 

#Each person should pay (150.00 / 5) * 1.12 = 33.6
#Format the result to 2 decimal places = 33.60

#Tip: There are 2 ways to round a number. You might have to do some Googling to solve this.💪

#Write your code below this line 👇

print("Welcome to the tip calculator.")
total_bill = float(input("What was the total bill? $"))
percentage_bill = int(input("What percentage tip would you like to give? 10, 12, or 15? "))
people_bill = int(input("How many people to split the bill? "))


tip = percentage_bill / 100
tipbill = total_bill * tip
percentagetip = tipbill + total_bill
peopletip = percentagetip / people_bill
total_each = round(peopletip, 2)
complete = f"Each person should pay: ${total_each}"

print(complete)