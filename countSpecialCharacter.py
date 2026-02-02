# st = "python@123#"
# count = 0

# for ch in st:
#     if not (('a' <= ch <= 'z') or ('A' <= ch <= 'Z') or ('0' <= ch <= '9')):
#         count += 1

# print(count)




st = "python@123#"
count = 0

for ch in st:
    if not ch.isalnum():
        count += 1

print(count)

