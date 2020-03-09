# 1. Write a Python program to print the
# following string in a specific format
# Sample String : "Twinkle, twinkle, little star,
# How I wonder what you are! Up above the world so high,
# Like a diamond in the sky. Twinkle, twinkle, little star,
# How I wonder what you are"

print("Twinkle, twinkle, little star, "
      "\n\tHow I wonder what you are! "
      "\n\t\tUp above the world so high, "
      "\n\t\tLike a diamond in the sky. "
      "\nTwinkle, twinkle, little star, "
      "\n\tHow I wonder what you are")

name = "Hemangi"
tasks = 2
print("Hello " + name + ". How are you today?")
print("Hello {}. You have {} task to finish today."
      .format(name, tasks))

data = (name, tasks)
print("Hello {0}. You have {1} task to finish today."
      .format(data))
