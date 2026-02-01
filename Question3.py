# Print vowel

# st = "Welcome to the python string"
# for ch in st:
#     # if ch.lower() in "aeiou":
#     #     print(ch, end=" ")
#     if ch in "aeiou" or ch in "AEIOU":
#         print(ch, end=" ")


# count vowels and consonants

st = "Python"
v = c = cp = 0

for ch in st:
    if ch.lower() in "aeiou":
        v += 1
    elif ch.isupper():
        cp += 1
    elif ch.isalpha():
        c += 1

print("Vowels:", v)
print("Consonants:", c)
print("Capital letters:", cp)

