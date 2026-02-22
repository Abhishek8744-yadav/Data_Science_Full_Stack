# Question 9: Create a tuple of first 5 even numbers
print("\nQuestion 9: Create a tuple of first 5 even numbers")
count=[]
for i in range(1,100):
    if i%2==0:
        count.append(i)
        if len(count)>=5:
            break
print(f"The First 5 even number Tuple is:- {count}")

