# Convert string to title case without using .title()

st = "Welcome to the python world"
res = ""
words = st.split()

for w in words:
    res += w[0].upper() + w[1:] + " "
    
print(res)