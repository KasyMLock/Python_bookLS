def starts_with(string, prfx):
    return string.startswith(prfx)


print(starts_with("launch", "la"))   # True
print(starts_with("school", "sah"))  # False
print(starts_with("school", "sch"))  # True    