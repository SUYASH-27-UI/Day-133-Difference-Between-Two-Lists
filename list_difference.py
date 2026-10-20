list1 = [10, 20, 30, 40, 50]
list2 = [30, 40, 50, 60, 70]

difference = []

for number in list1:
    if number not in list2:
        difference.append(number)

print("First list:", list1)
print("Second list:", list2)
print("Difference:", difference)
