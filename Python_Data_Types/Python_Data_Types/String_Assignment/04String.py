# Question : Remove all punctuation from "Hello, World! How are you?"
import string

sen = "Hello, World! How are you?"

# Create a translation table that maps every punctuation character to None
translator = str.maketrans('', '', string.punctuation)
cleaned_text = sen.translate(translator)

print(cleaned_text)