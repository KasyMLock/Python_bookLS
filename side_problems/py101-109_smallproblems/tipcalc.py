#tip calculator
print("....................................................................")
bill = float(input("Hey there User, please enter the bill amount: "))
percentage = float(input("and what percentage would you like to tip?: "))

tip = bill * (percentage / 100)
total = bill + tip


print(F"The tip is ${tip:.2f}")
print(F"Total is ${total:.2f}")
print("....................................................................")
