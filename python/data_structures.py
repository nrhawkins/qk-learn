# data structures / complexity / methods /

# Lists / Arrays

# List Comprehensions - way to create new lists based on existing lists
# https://realpython.com/list-comprehension-python/
# faster than normal functions and loops
# more compact, easier to read, don't use complex or nested ones if it's hard to read
# can also use for mapping and filtering
square_roots = [0, 1, 2, 3, 4, 5]
squares = [x*x for x in square_roots if x > 0 and x % 2 == 0]
print(squares)

# Linked Lists

# Queues and Stacks
wait_line = ["Al", "Bob", "Chia", "Dawg"]
mail_stack = ["CityLight", "PSE", "Mom", "Wired", "Ninety-Nines"]

first_customer = wait_line.pop(0)

assert(first_customer == "Al")
assert(wait_line[0] == "Bob")

wait_line.append("Ralph")
assert(wait_line[-1] == "Ralph")

# Hash Set
# Set Comprehensions - example, find unique vowels
greeting = "Hello, Welcome to Our Home Island!"
unique_vowels = {l.lower() for l in greeting if l.lower() in "aeiou"}
print(unique_vowels)
assert unique_vowels == {"a","e","i","o","u"}
# Hash Map - Dictionary
# Other types of Dictionaries - defaultdict
# Dictionary Comprehensions

# Binary Tree

# Binary Heap - min, max

# Complexity
