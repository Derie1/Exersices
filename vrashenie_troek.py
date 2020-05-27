def rotate_left(tuple):
    a = tuple[0]
    b = tuple[1]
    c = tuple[2]
    # (a, b, c) = (b, c, a)
    return (b, c, a)

def rotate_right(tuple):
    a = tuple[0]
    b = tuple[1]
    c = tuple[2]
    return (c, a, b)

# tuple = input('Введите кортеж из трёх элементов')
