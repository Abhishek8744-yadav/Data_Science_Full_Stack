# Question 8: Calculate the average of numbers: 15, 23, 31, 42, 56
print("\nQuestion 8: Calculate the average of numbers: 15, 23, 31, 42, 56")

num=[15, 23, 31, 42, 56]

length=len(num)

avg=0

for i in num:
    avg+=i
result=avg/length

print(result)

