'''Write and test three functions that each take two words (strings) as parameters and
return sorted lists (as defined above) representing respectively:
Letters that appear in at least one of the two words.
Letters that appear in both words.
Letters that appear in either word, but not in both.'''

def letters_in_either(word1, word2):
    return sorted(set(word1) | set(word2))
def letters_in_both(word1, word2):
    return sorted(set(word1) & set(word2))
def letters_in_one_only(word1, word2):
    return sorted(set(word1) ^ set(word2))

# Test
word1 = input("Enter the first word: ")
word2 = input("Enter the second word: ")
print(f"Letters in at least one of the two words: {letters_in_either(word1, word2)}")
print(f"Letters in both words: {letters_in_both(word1, word2)}")
print(f"Letters in either word but not in both: {letters_in_one_only(word1, word2)}")

