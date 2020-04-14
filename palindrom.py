# Проще всего применить функцию list.reverse и сравнить с исходным списком
def is_palindrom(name):
    # reverse_name = name.reverse()
    if name == '':
        return True
    reverse_name = []
    lenght = len(name) - 1

    while lenght >= 0:
        reverse_name = reverse_name.append(lenght)
        lenght -= 1

    if name == reverse_name:
        return True
    else:
        return False

name = input('Введите строку: ', )
is_palindrom(name)
