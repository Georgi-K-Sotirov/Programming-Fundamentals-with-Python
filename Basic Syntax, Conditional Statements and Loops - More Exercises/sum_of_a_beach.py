word_input = input()
word = word_input.lower()
counter = 0
counter += word.count("sand")
counter += word.count("water")
counter += word.count("fish")
counter += word.count("sun")
print(counter)