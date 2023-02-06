# True если поступившая на вход строка является правильной скобочной последовательностью

def is_correct_bracket(text):
    counter = 0
    for i in range(len(text)):
        if counter < 0:
            return False
        if text[i] == '(':
            counter += 1
        elif text[i] == ')':
            counter -= 1
    if counter != 0:
        return False
    return True

print(is_correct_bracket(input()))