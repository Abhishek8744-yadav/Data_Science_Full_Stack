# Question 8: Check if 25 exists in tuple (10, 20, 30, 40, 50)
print("\nQuestion 8: Check if 25 exists in tuple (10, 20, 30, 40, 50)")

num=(10, 20, 30, 40, 50)

for i in num:
    if 25 in num:
        print("Found")
        break
else:
    print("NOT Found!!!")
