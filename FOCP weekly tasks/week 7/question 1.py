'''Write and test a function that takes a string as a parameter and returns a sorted list
of all the unique letters used in the string. So, if the string is cheese, the list
returned should be ['c', 'e', 'h', 's'].
'''

def unique_letters(s):
    return sorted(set(s))

# Test
string = input("Enter a string: ")
print(f"Unique letters: {unique_letters(string)}")
