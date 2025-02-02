print("type starting even number")
start_number = int(input())
print("type end of range number")
last_number = int(input())
print("_______________________________________")

for number in range(start_number, last_number, 2):
    if number % 2 == 1:
        print(number + 1)
    else: print(number)