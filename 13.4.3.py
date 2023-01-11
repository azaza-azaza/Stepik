def find_all(text, letter):
    how_many = text.count(letter)
    places = list()
    start = 0
    for i in range(how_many):
        start = text.find(letter, start)
        places.append(text.find(letter, start+1)+i)

    return places


text = input()
letter = input()
print(find_all(text, letter))
# print(find_all(a,b))

