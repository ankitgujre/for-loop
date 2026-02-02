st = "programming"
seen = ""

for ch in st:
    if ch in seen:
        print(ch)
        break
    else:
        seen += ch
