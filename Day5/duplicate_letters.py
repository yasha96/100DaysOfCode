def has_duplicate_letters(sentence):
    words = sentence.split()
    
    for word in words:
        letter_set = set()
        for letter in word.lower():
            if letter in letter_set:
                return True
            letter_set.add(letter)
    
    return False
user_input = input("Enter a sentence: ")
result = has_duplicate_letters(user_input)
print(result)

