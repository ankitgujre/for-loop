# wap to check anagram

st1 = input("Enter 1st string: ")
st2 = input("Enter 2nd string: ")

if len(st1) != len(st2):
    print("Not Anagram")
else:
    freq1 = {}
    freq2 = {}

    for ch in st1:
        if ch in freq1:
            freq1[ch] += 1
        else:
            freq1[ch] = 1

    for ch in st2:
        if ch in freq2:
            freq2[ch] += 1
        else:
            freq2[ch] = 1

    if freq1 == freq2:
        print("Anagram")
    else:
        print("Not Anagram")
