# Question : Count consonants in "Hello World"
count=""
con_so='Hello World'
vowels="AEIOUaeiou"
for i in con_so:
    if i not in vowels:
        count+=i
print(count)