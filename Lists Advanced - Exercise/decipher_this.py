def decipher(word):
    code = [char for char in word if char.isdigit()]
    code_digit = int("".join(code))
    new_word = chr(code_digit) + word[len(code):]
    new_word = [char for char in new_word]
    new_word[1], new_word[-1] = new_word[-1], new_word[1]
    new_word = "".join(new_word)
    return new_word


code_words = input().split()
code_message = [decipher(word) for word in code_words]
print(' '.join(code_message))