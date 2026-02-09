# Question 6: Check if 97 is a prime number
print("\nQuestion 6: Check if 97 is a prime number")


number=int(input("Enter Your Number:-"))

if number<=1:
    print("Not a Prime Number")
else:
    for i in range (2,number):
        if number%i==0:
            print("Not a Prime Number")
            break
    else:
        print("Prime Number") 
