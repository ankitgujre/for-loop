nums = [10, 5, 21, 20, 8]

# second largest DISTINCT value (so 20,20 -> second largest is 10)
largest = None
second = None

for x in nums:
    if largest is None or x > largest:
        if largest != x:          # avoid duplicate promotion
            second = largest
        largest = x
    elif x != largest and (second is None or x > second):
        second = x

if second is None:
    print("No second largest distinct number (need at least two distinct values).")
else:
    print("Second largest:", second)
