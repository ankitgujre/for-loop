st = "welcome to python"
res = ""

for ch in st:
    if ch == " ":
        res += "_"
    else:
        res += ch

print(res)
