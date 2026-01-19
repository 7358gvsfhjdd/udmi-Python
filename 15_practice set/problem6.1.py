
'''Write a program that takes a list of numbers and removes all duplicates using a set.'''
# Input list with duplicates
numbers = [1, 2, 3, 4, 2, 3, 5, 6, 1]

# Remove duplicates using set
unique_numbers = list(set(numbers))

# Print result
print("List after removing duplicates:", unique_numbers)
