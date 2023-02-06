def is_one_away(word1, word2):
    if len(word1) != len(word2):
        return False
    counter = 0
    for el in range(len(word1)):
        if word1[el] != word2[el]:
            counter += 1
    if counter != 1:
        return False
    return True


print(is_one_away(input(), input()))