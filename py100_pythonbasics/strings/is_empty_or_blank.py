def is_empty_or_blank(string):
    if len(string) == 0: return True
    elif ' ' in string: return True
    else: return False


print(is_empty_or_blank('mars'))  # False
print(is_empty_or_blank('  '))    # True
print(is_empty_or_blank(''))      # True

print('12131343242113211'.strip('12'))