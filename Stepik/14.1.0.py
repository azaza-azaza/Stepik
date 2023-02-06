def draw_triangle():
    stars = 1
    space = 7
    for i in range(8):
        print(' ' * space + '*' * stars)
        stars += 2
        space -= 1
    print()
draw_triangle()