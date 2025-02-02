def first(list):
    return list[0]

#next excersise

def last(list):
    if len(list) > 0: return list[-1]
    else: return 'Nothing in this list.'

#next excersise

energy = ['fossil', 'solar', 'wind', 'tidal', 'fusion']


energy.remove('fossil')
energy.append('geothermal')

#next excersise

alphabet = 'abcdefghijklmnopqrstuvwxyz'

#next excersise


scores = [196, 47, 113, 190, 100, 102]
count = 0

for score in scores:  
    if score >= 100: count += 1

#next excersise

vocabulary = [
    ['happy', 'cheerful', 'merry', 'glad'],
    ['tired', 'sleepy', 'fatigued', 'drained'],
    ['excited', 'eager', 'enthused', 'animated'],
]



#next excersise



destinations = ['Prague', 'London', 'Sydney', 'Belfast',
                'Rome', 'Aruba', 'Paris', 'Bora Bora',
                'Barcelona', 'Rio de Janeiro', 'Marrakesh',
                'New York City']


def contains(word, list):
    for check in list:
        if word == check: 
            return True
            break
    
    else: return False

#next excersise

passcode = ['11', 'jZ5', 'hQ3f*', '8!7g3', 'p3Fs']

print('-'.join(passcode))

#next excersise

grocery_list = ['paprika', 'tofu', 'garlic', 'quinoa',
                'carrots', 'broccoli', 'hummus']


while grocery_list:
    item = grocery_list.pop(0)
    print(item)
    

print(grocery_list)