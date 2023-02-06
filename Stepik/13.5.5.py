def is_palindrome(text):
    pure_text = ''
    for el in range(len(text)):
        if text[el].isalpha():
            pure_text += text[el]
    pure_text = pure_text.lower()
    # return pure_text
    for i in range(len(pure_text)//2):
        if pure_text[i] != pure_text[-i-1]:
            return False
    return True

print(is_palindrome(input()))


