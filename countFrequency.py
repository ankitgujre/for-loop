# count frequency of each character

st = "count frequency of each character"
freq = {}

for ch in st:
    if ch in freq:
        freq[ch] += 1
    else:
        freq[ch] = 1

print(freq)
