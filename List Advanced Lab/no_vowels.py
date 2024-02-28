def no_vowels():
    word = input()

    new_word = [char for char in word if char.lower() not in ['a', 'o', 'u', 'e', 'i']]

    return new_word


print(''.join(no_vowels()))