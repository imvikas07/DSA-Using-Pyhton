
'''
In Python, a list is a versatile and widely used data structure that allows you to store a collection,
of items. Lists are ordered, mutable (modifiable), and can contain elements of different data types, 
such as integers, strings, floats, and even other lists. Here's an in-depth explanation of Python lists
with examples:

'''



### Creating a List
'''
You can create a list in Python by placing comma-separated values inside square brackets `[]`.
'''

# Creating a list of integers
numbers = [1, 2, 3, 4, 5]

# Creating a list of strings
fruits = ["apple", "banana", "cherry"]

# Creating a list with mixed data types
mixed_list = [10, "hello", 3.14, True]


### Accessing Elements
#You can access elements of a list using square brackets `[]` with indices. Python uses zero-based indexing, meaning the first element is at index 0.

fruits = ["apple", "banana", "cherry"]

print(fruits[0])  # Output: "apple"
print(fruits[1])  # Output: "banana"

#You can also use negative indices to access elements from the end of the list:


print(fruits[-1])  # Output: "cherry"


### Slicing
#Slicing allows you to create a new list from a subset of an existing list. It uses the syntax `list[start:stop:step]`.

numbers = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]

# Get a sublist from index 2 to index 5 (exclusive)
sublist = numbers[2:5]
print(sublist)  # Output: [2, 3, 4]

# Get every second element
every_other = numbers[::2]
print(every_other)  # Output: [0, 2, 4, 6, 8]

# Reverse the list
reversed_list = numbers[::-1]
print(reversed_list)  # Output: [9, 8, 7, 6, 5, 4, 3, 2, 1, 0]


### Modifying Lists
#Lists are mutable, meaning you can change, add, or remove elements after creating the list.

#### Changing Elements

#You can change the value of a specific element by accessing it through its index.

fruits = ["apple", "banana", "cherry"]
fruits[1] = "orange"
print(fruits)  # Output: ["apple", "orange", "cherry"]


#### Adding Elements
#You can add elements to the end of a list using the `append()` method:


fruits = ["apple", "banana", "cherry"]
fruits.append("orange")
print(fruits)  # Output: ["apple", "banana", "cherry", "orange"]


#You can also insert elements at a specific position using `insert()`:

fruits.insert(1, "grape")
print(fruits)  # Output: ["apple", "grape", "banana", "cherry", "orange"]


#### Removing Elements
#You can remove elements by their value using `remove()`:

fruits.remove("banana")
print(fruits)  # Output: ["apple", "grape", "cherry", "orange"]


#If you know the index of the element you want to remove, you can use `pop()`:

popped_item = fruits.pop(2)  # Removes and returns the item at index 2
print(fruits)  # Output: ["apple", "grape", "orange"]
print(popped_item)  # Output: "cherry"


#### List Concatenation and Repetition
#You can concatenate two lists using the `+` operator:

list1 = [1, 2, 3]
list2 = [4, 5, 6]
concatenated = list1 + list2
print(concatenated)  # Output: [1, 2, 3, 4, 5, 6]


#You can also repeat a list using the `*` operator:

repeated = [0] * 3
print(repeated)  # Output: [0, 0, 0]


### List Methods
#Python provides many built-in methods to work with lists. Here are a few commonly used ones:

-# `append()`: Adds an element to the end of the list.
- #`insert()`: Inserts an element at a specified position.
- #`remove()`: Removes the first occurrence of a specified value.
- #`pop()`: Removes the element at a specified position or the last element if no index is specified.
- #`index()`: Returns the index of the first occurrence of a specified value.
- #`count()`: Returns the number of occurrences of a specified value.
- #`sort()`: Sorts the list in ascending order.
- #`reverse()`: Reverses the order of the list.

numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]

numbers.sort()  # Sorts the list in-place
print(numbers)  # Output: [1, 1, 2, 3, 4, 5, 5, 6, 9]

numbers.reverse()  # Reverses the list in-place
print(numbers)  # Output: [9, 6, 5, 5, 4, 3, 2, 1, 1]

print(numbers.count(5))  # Output: 2 (count of occurrences of 5)

### List Comprehensions
'''
List comprehensions provide a concise way to create lists in Python. 
They consist of an expression followed by a `for` clause, and optionally `if` clauses.
'''

#### Example 1: Squares of Numbers

squares = [x**2 for x in range(10)]
print(squares)  # Output: [0, 1, 4, 9, 16, 25, 36, 49, 64, 81]


#### Example 2: Filtered List

numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_numbers = [x for x in numbers if x % 2 == 0]
print(even_numbers)  # Output: [2, 4, 6, 8, 10]

#List comprehensions are a powerful and efficient way to work with lists in Python.

#Lists are fundamental to Python programming, and mastering their use will greatly enhance your ability to work with collections of data.