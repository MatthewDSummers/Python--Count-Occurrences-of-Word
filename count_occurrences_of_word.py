import re
# A function to return a dictionary containing the words of a string as its keys and their values as a count of each time the word occurred in the string
def count_occurrences_of_word(text):
    if isinstance(text, str):
        text = text.lower()
        word_dict = {}
        for word in re.findall(r'\b\w+\b', text): # get each word of the string, ignoring non-alphanumeric symbols
            word_dict[word] = word_dict.get(word, 0) + 1 # if word is a key in the dict, it increments its value by 1; otherwise, it adds it to the dict with a val of 1
        return word_dict
    else:
        return "Please input a string"

print(count_occurrences_of_word("I am counting your words WORDS, ok? OK!"))
# output: {'i': 1, 'am': 1, 'counting': 1, 'your': 1, 'words': 2, 'ok': 2}