print(".................................................................................")
print("hello user")
print("this program is designed to calculate a room's square footage and square meterage")

options = ['feet', 'Feet', 'FEET', 'Meter', 'METERS', 'meters', 'Meters']
control = 0


while control == False:
    option = str(input("would you like this in meters or feet?: "))

    if option in options: 
        control = 1
    elif option == "quit" or option == "exit" or option == "q":
        break 
    else: 
        print('.................................................................................')
        print(F"{option} is an invalid option, try either 'meters' or 'feet'.")
        continue

    length = float(input(F"what is the length of the room in {option}?: "))
    width = float(input(F"what is the width of the room in {option}?: ")) 
    print(".....................................................................................")

    area = length * width
   

    if option == "feet" or option == "Feet" or option == "FEET":
        print(F"The area of the room in question is {area:.2f} square feet or ({area / 10.7639:.2f}sq.mtrs)")
       

    elif option == "meters" or option == "meter" or option == "Meters" or option == "METERS":
        print(F"The area of the room in question is {area:.2f} square meters or ({area * 10.7639:.2f}sq.ft)")
        

    else: 
        print(F"{option} is an invalid answer, I don't know how we got this far lol!")
        


