
# Arrays in Python

## Using the `array` module
"""

In Python, an array is a data structure that stores a collection of items. Unlike lists, arrays can only store elements of the same data type, such as integers or floats. Arrays offer advantages in terms of memory efficiency and performance for numerical computations compared to lists, especially when dealing with large datasets.

Python doesn't have a built-in array data structure in its standard library, but you can use the `array` module, as well as the `numpy` library for more advanced array manipulation. Let's break down each of these:

"""
### 1. Using the `array` module

#The `array` module provides a way to create arrays in Python. Here's how you can use it:


import array

# Create an array of integers
int_array = array.array('i', [1, 2, 3, 4, 5])

# Access elements of the array
print(int_array[0])  # Output: 1

# Append elements to the array
int_array.append(6)

# Remove elements from the array
int_array.remove(3)

# Find the index of an element
index = int_array.index(4)
print(index)  # Output: 2


'''
In this example, `array.array('i', [1, 2, 3, 4, 5])` creates an array of integers with initial values `[1, 2, 3, 4, 5]`. The first argument `'i'` specifies the type code, which indicates that the array will store integers.

'''
### 2. Using the `numpy` library


'''
`numpy` is a powerful library for numerical computing in Python. It provides a multidimensional array object called `ndarray`, which offers more functionality and flexibility compared to the `array` module.
'''

import numpy as np

# Create a numpy array
np_array = np.array([1, 2, 3, 4, 5])

# Access elements of the array
print(np_array[0])  # Output: 1

# Append elements to the array
np_array = np.append(np_array, 6)

# Remove elements from the array
np_array = np.delete(np_array, 2)

# Find the index of an element
index = np.where(np_array == 4)
print(index)  # Output: (array([2]),)


'''
Here, `np.array([1, 2, 3, 4, 5])` creates a numpy array with initial values `[1, 2, 3, 4, 5]`. Numpy provides various functions for array manipulation, such as `append()`, `delete()`, and `where()`.

'''
'''
Both the `array` module and `numpy` library offer methods and functions for common array operations, including:
'''
#- Accessing elements
#- Appending elements
#- Removing elements
#- Finding elements

## These are just some of the basic operations you can perform with arrays in Python. Depending on your specific use case and requirements, you may choose between the `array` module and `numpy` library for array manipulation.

## List Methods in Python

##In Python, arrays are typically represented using lists. Lists are ordered collections of items, and Python provides several built-in methods to manipulate them. Here's an explanation of some common list methods in Python:


# append(): Adds an element to the end of the list.
fruits = ['apple', 'banana', 'orange']
fruits.append('grape')
print(fruits)  # Output: ['apple', 'banana', 'orange', 'grape']

# extend(): Extends the list by appending elements from another iterable.
fruits = ['apple', 'banana', 'orange']
fruits.extend(['grape', 'kiwi'])
print(fruits)  # Output: ['apple', 'banana', 'orange', 'grape', 'kiwi']

# insert(): Inserts an element at a specified index.
fruits = ['apple', 'banana', 'orange']
fruits.insert(1, 'grape')
print(fruits)  # Output: ['apple', 'grape', 'banana', 'orange']

# remove(): Removes the first occurrence of a specified value from the list.
fruits = ['apple', 'banana', 'orange']
fruits.remove('banana')
print(fruits)  # Output: ['apple', 'orange']

# pop(): Removes the element at a specified index and returns it.
fruits = ['apple', 'banana', 'orange']
removed_fruit = fruits.pop(1)
print(removed_fruit)  # Output: 'banana'
print(fruits)  # Output: ['apple', 'orange']

# index(): Returns the index of the first occurrence of a specified value.
fruits = ['apple', 'banana', 'orange']
index = fruits.index('banana')
print(index)  # Output: 1

# count(): Returns the number of occurrences of a specified value in the list.
fruits = ['apple', 'banana', 'banana', 'orange']
count = fruits.count('banana')
print(count)  # Output: 2

# sort(): Sorts the list in ascending order.
numbers = [3, 1, 4, 1, 5, 9, 2, 6, 5]
numbers.sort()
print(numbers)  # Output: [1, 1, 2, 3, 4, 5, 5, 6, 9]

# reverse(): Reverses the elements of the list in place.
fruits = ['apple', 'banana', 'orange']
fruits.reverse()
print(fruits)  # Output: ['orange', 'banana', 'apple']


"""
These are just a few examples of Python list methods. Python provides many more built-in methods,
for lists, and you can also create your own functions to manipulate lists in custom ways.
"""
