from collections import Counter
import re

def get_top_10_words(paragraph):
    # Tokenize the paragraph into words using regular expressions
    words = re.findall(r'\b\w+\b', paragraph.lower())  # Convert to lowercase for case insensitivity

    # Count the frequency of each word
    word_count = Counter(words)

    # Get the top 10 most common words
    top_10_words = word_count.most_common(10)

    return top_10_words

# Prompt the user for input
paragraph = input("Enter a paragraph: ")

top_words = get_top_10_words(paragraph)

# Print the top 10 words and their frequencies
for word, frequency in top_words:
    print(f"{word}: {frequency}")

