def palindrome(list_of_words, key_word):
    palindrome_list = [word for word in list_of_words if word == word[::-1]]
    key_counter = palindrome_list.count(key_word)
    return palindrome_list, key_counter


words = input().split(" ")
key = input()

result = palindrome(words, key)

print(result[0])
print(f"Found palindrome {result[1]} times")