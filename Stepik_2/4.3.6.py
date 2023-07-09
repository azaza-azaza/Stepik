

def chunked(num, text):

    burn = list()
    if len(text) < num:
        test_list_3 = list()
        for j in range(len(text)):
            test_list_3 += text[j]
        burn.append(test_list_3)
    elif len(text) >= num:
        for i in range(num-1, len(text), num):
            test_list = list()
            for n in range(num-1, -1, -1):
                test_list += text[i-n]

            burn.append(test_list)
            test_list = list()
    if len(text) % num != 0 and len(text) > num:
        whole_number = len(text) // num
        for k in range(whole_number*num, len(text)):
            test_list_2 = list()
            test_list_2 += text[k]
        burn.append(test_list_2)


    return burn

text = [c for c in input().split()]
num = int(input())

print(chunked(num, text))