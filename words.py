LIST_OF_WORDS = ['apple', 'banana', 'japan', 'brz', 'egypt', 'England']

def print_upper_words(words):

    """Takes a list of words and uppercases the words that start with e"""

    for word in words:
        if(word[0] in ['e', 'E']):
            print(word.upper())

print_upper_words(LIST_OF_WORDS)

def print_upper_words2(words, must_start_with):

    """Takes a list of words and only uppercases and prints the words that start with the letters assigned in the must_start_with variable"""

    for word in words:
        for letter in must_start_with:
            if(word[0] == letter):
                print(word.upper())

# this should print "HELLO", "HEY", "YO", and "YES"

print_upper_words2(["hello", "hey", "goodbye", "yo", "yes"],
                   must_start_with={"h", "y"})
