# Question: Find the shortest word in "Python is a programming language"
word="Python is a programming language"

slogan=word.split()

shortest_word=slogan[0]

for i in slogan:

    if len(i)<len(shortest_word):

        shortest_word=i


print(f"The Shortest Word In {word} is:-  {shortest_word}")