data = []
with open("file.txt") as f:
    for line in f:
        data += [float(x) for x in line.split()]


def minimum(list_name):
    n = float('+inf')
    for num in list_name:
        if num < n:
            n = num
    print("Минимально число в файле равно", n)
    return n


def maximum(list_name):
    k = float('-inf')
    for num in list_name:
        if num > k:
            k = num
    print("Максимальное число в файле равно", k)
    return k


def summa(list_name):
    s = 0
    for num in list_name:
        s += num
    print("Сумма чисел в файле равна", s)
    return s


def multiplication(list_name):
    m = 1
    for num in list_name:
        try:
            m *= num
        except OverflowError:
            print("Произошла ошибка переполнения, уменьшите количество чисел в файле и их величину")
            raise
    print("Произведение чисел в файле равно", m)
    return m


minimum(data)
maximum(data)
summa(data)
multiplication(data)
