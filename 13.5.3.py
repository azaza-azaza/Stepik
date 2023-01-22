def is_password_good(password):
    if (len(password) > 7 and password.islower() == False and
            password.isupper() == False and
            password.isalpha() == False and
            password.isdigit() == False and
            password.isalnum()):
        return True
    else:
        return False

print(is_password_good(input()))