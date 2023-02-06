def is_valid_triangle(side1, side2, side3):
    if side1 + side2 > side3 and side2 + side3 > side1 and side3 + side1 > side2:
        return True
    else:
        return False

print(is_valid_triangle(int(input()), int(input()), int(input())))
