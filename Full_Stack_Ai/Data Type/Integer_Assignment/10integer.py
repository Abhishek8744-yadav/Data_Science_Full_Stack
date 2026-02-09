# Question 10: Calculate the sum of first 20 odd numbers
print("\nQuestion 10: Calculate the sum of first 20 odd numbers")

count=0
sum = 0
for i in range(1,1000):
    if i%2 !=0:
        count+=1  ##-----> count variable count the odd number till upto 20
        sum+=i    ##-----> sum variable taking the sum of all 20 odd numbers 
        if count==20:
            break  

print(f"The Sum of first {count} Odd number is:- {sum}")
    
       