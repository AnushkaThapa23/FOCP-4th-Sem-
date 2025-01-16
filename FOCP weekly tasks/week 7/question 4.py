'''One approach to analysing some encrypted data where a substitution is suspected
is frequency analysis. A count of the dierent symbols in the message can be used
to identify the language used, and sometimes some of the letters. In English, the
most common letter is "e", and so the symbol representing "e" should appear most
in the encrypted text.
Write a program that processes a string representing a message and reports the six
most common letters, along with the number of times they appear. Case should
not matter, so "E" and "e" are considered the same'''


from collections import Counter

def frequency_analysis(text):
    counts = Counter(char for char in text.lower() if char.isalpha())
    return counts.most_common(6)

# Test
text = input("Enter the text to analyze: ")
analysis = frequency_analysis(text)
print("Most common letters and their counts:")
for letter, count in analysis:
    print(f"{letter}: {count}")
