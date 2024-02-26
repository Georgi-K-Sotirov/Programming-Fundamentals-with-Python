def char_from_ascii(num1,num2):
    result = ''
    for i in range(num1 + 1, num2):
        result += chr(i) + " "
    return result


first_chr = input()
second_chr = input()
print(char_from_ascii(ord(first_chr), ord(second_chr)))