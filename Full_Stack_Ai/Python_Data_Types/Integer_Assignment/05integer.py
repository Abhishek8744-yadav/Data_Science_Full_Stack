# Question 5: Calculate the sum of digits in number 12345
print("\nQuestion 5: Calculate the sum of digits in number 12345")

data = 12345
sum=0
new_data = str(12345)

for i in new_data:
    sum = sum + int(i)

print(f"The Sum Of 12345 is :- {sum}")


