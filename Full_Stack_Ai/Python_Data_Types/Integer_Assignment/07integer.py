# Question 7: Find the factorial of 8
print("\nQuestion 7: Find the factorial of 8")

num = int(input("Enter your Number :-"))

factorial =1
for i in range(1,num+1):
    factorial=factorial*i
    
print(factorial)