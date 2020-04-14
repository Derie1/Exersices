def fib(n):
    if n < 0:
        result = 'Введенное число меньше 0'
        return result
    elif n == 0:
        result = 0
        return result
    elif n == 1:
        result = 1
        return result
    else:
        result = 0
        i = 2
        f_1 = 1
        f_2 = 0
        while i <= n:
            result = f_1 + f_2
            f_2 = f_1
            f_1 = result
            i = i + 1
    return result
number = input('Введите число: ', )
print(fib(int(number)))
