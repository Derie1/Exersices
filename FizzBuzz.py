def fizz_buzz(first_num, last_num):
    if first_num > last_num:
        return ''
    list1 = range(first_num, last_num + 1)
    list = []
    for i in list1:
        if i % 3 == 0 and i % 5 == 0:
            list.append('FizzBuzz')
        elif i % 3 == 0:
            list.append('Fizz')
        elif i % 5 == 0:
            list.append('Buzz')
        else:
            list.append(i)
    return list

print(fizz_buzz(15, 18))
