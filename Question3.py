# Print vowel and consonant

st = "Welcome to the python string"
for ch in st:
    # if ch.lower() in "aeiou":
    #     print(ch, end=" ")
    if ch in "aeiou" or ch in "AEIOU":
        print(ch, end=" ")
