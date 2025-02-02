sentence = 'launch school tech & talk'

def capitalize_words(sentence):
    count = 0
    list_sentence = sentence.split()
    for word in list_sentence:
        list_sentence[count] = word[0].upper() + word[1:]
        count += 1
    sentence = ' '.join(list_sentence)
    return sentence

print(capitalize_words("""i have built an algorithm to capatalize, 
                       the begining of each word!"""))