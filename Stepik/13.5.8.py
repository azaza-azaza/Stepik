def convert_to_python_case(text):
    python_text = text[0].lower()
    for i in range(1, len(text)):
        if text[i].isupper():
            python_text += '_' + text[i].lower()
        else:
            python_text += text[i]

    return python_text

print(convert_to_python_case(input()))