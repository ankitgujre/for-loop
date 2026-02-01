# WAP for check palindrome or not

st = input("Enter string: ")

rev = ""
for ch in st:
    rev = ch + rev
if st == rev:
    print("Palindrome")
else:
    print("Not palindrome")