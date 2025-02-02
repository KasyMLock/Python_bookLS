print("starting number of range?")
usersays1 = int(input())
print("finishing number of range?")
usersays2 = int(input())

for n in range(usersays1, usersays2):
    if n % 2 > 0:
        print(n)