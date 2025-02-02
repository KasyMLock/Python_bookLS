def find_first_nonzero_among(numbers):
    for n in numbers: #why doesn't the list return the 2 as well? 
        if n != 0:
            return n
            
            
       



# Next Excersise 

import random

def predict_weather():
    sunshine = random.choice([True, False])

    if sunshine:
        print("Today's weather will be sunny!")
    else:
        print("Today's weather will be cloudy!")


# Next Excersise 

def multiply_by_five(n):
    return n * 5

# Next Excersise 

pets = { 'cat': 'pepe', 'dog': ['sparky', 'fido'], 'fish': 'oscar' }

pets['dog'].append('bowser')


# next excersise

def get_quote(person):
    if person == 'Yoda':
        return 'Do. Or do not. There is no try.'
    if person == 'Confucius':
        return 'I hear and I forget. I see and I remember. I do and I understand.'
    if person == 'Einstein':
       return 'Do not worry about your difficulties in Mathematics. I can assure you mine are still greater.'


#next excersise

numbers = []

for i in range(1,6):
    numbers.append(i)


#next exersise



#next exersise

sub_list = ["-", "-", "-"]
matrix = []

for _ in range(3):
    matrix.append(sub_list.copy())

matrix[0][0] = "X"

#next exersise

def find_maximum(numbers):
    if not numbers:
        return None
    max_number = numbers[0]
    for number in numbers:
        if number > max_number:
            max_number = number
    return max_number

# next excersise

def digit_product(str_num):
    digits = [int(n) for n in str_num]
    product = 1

    for digit in digits:
        product *= digit

    return product

result = digit_product('12345')
print(result)  # expected: 120, actual: 0