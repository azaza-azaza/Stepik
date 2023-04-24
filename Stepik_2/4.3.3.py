n = int(input())+1

def pascal(num):
    row = [1, 1]
    if num == 1:
        row = [1]
    elif num == 2:
        row = [1, 1]
    else:
        for i in range(2, num):
            row_1 = [1]
            for j in range(len(row)-1):
                num_1 = row[j] + row[j + 1]
                row_1.append(num_1)
            row_1.append(1)
            row = row_1
    return row

print(pascal(n))


