# example 1
square = lambda x: x * x
print(square(5))  

# example 2
add = lambda x, y: x + y
print(add(3, 7))  

# example 3
max_val = lambda x, y: x if x > y else y
print(max_val(8, 5))  

# Sorted
words = ["python", "ai", "lambda", "decorator"]
sorted_words = sorted(words, key=lambda word: len(word))
print(sorted_words)  

pairs = [(1, 3), (2, 1), (5, 0)]
sorted_pairs = sorted(pairs, key=lambda x: x[1])
print(sorted_pairs)  

#Map
nums = [1, 2, 3, 4]
squared = list(map(lambda x: x ** 2, nums))
print(squared)  

#Filter
nums = [1, 2, 3, 4, 5, 6]
evens = list(filter(lambda x: x % 2 == 0, nums))
print(evens)  

#Reduce
from functools import reduce

nums = [1, 2, 3, 4]
product = reduce(lambda x, y: x * y, nums)
print(product)  
