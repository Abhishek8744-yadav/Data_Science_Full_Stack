# Question : Convert "hello world" to "hElLo WoRlD" (alternating case)

text = "hello world"
result = "".join([char.upper() if i % 2 != 0 else char.lower() for i, char in enumerate(text)])

print(f"Alternating case : {result}")