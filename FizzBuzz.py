def fizz_buzz(first_num, last_num):
    for i in range(first_num, last_num):
        if i % 3 == 0 and i % 5 == 0:
            list.append('FizzBuzz')
        elif i % 3 == 0:
            list.append('Fizz')
        elif i % 5 == 0:
            list.append('Buzz')
            list.append('i')
        return list

fizz_buzz(3, 12)
