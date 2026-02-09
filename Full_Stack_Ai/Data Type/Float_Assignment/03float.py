# Question 3: Calculate the compound interest on $1000 at 5.5% for 3 years
print("\nQuestion 3: Calculate compound interest on $1000 at 5.5% for 3 years")


princple = 1000
rate = 5.5
time = 3

amount = princple*((1+(rate/100))**time)

CI = amount - princple

print(f"The Compound Intrest on {princple} at 5.5% is:- {CI:.2f}")
