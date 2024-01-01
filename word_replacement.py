

def word_replace():
    string = input("Enter your input string:")
    word_to_replace = input("Enter a string which needs to be replaced: ")
    new_word = input("Enter a string which is in new word: ")

    return string.replace(word_to_replace, new_word)

print(word_replace())