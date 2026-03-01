# Question 10: Find the average of numbers in tuple (15, 23, 31, 42, 56, 78)
print("\nQuestion 10: Find the average of numbers in tuple (15, 23, 31, 42, 56, 78)")

number=(15, 23, 31, 42, 56, 78)
sum=0
for i in number:
    sum+=i
    result=sum/len(numbers)

print(f"the average of numbers in tuple (15, 23, 31, 42, 56, 78) is:- {result}")

