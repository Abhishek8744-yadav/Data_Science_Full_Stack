# Question : Find all positions of 'a' in "banana"

text = "banana"
target = 'a'

# Use enumerate to get both the index (i) and the character (char)
positions = [i for i, char in enumerate(text) if char == target]

print(f"All positions of 'a' : {positions}")