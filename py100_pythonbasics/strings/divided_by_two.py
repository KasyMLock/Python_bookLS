numbers = {
    'high':   100,
    'medium': 50,
    'low':    10,
}



for number in numbers.items():

    key = number[0]
    value = number[1]
    message = F'A {key} number is {value}'
   
for a, b in numbers.items():
    print(f"A {a} number is {b}.")