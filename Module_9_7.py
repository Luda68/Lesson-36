"""Задание: Декораторы в Python

Цель задания:
Освоить механизмы создания декораторов Python.
Практически применить знания, создав функцию декоратор и обернув ею другую функцию.

Задание:
Напишите 2 функции:
Функция, которая складывает 3 числа (sum_three)
Функция декоратор (is_prime), которая распечатывает "Простое", если результат 1ой функции
будет простым числом и "Составное" в противном случае.
Примечания:
Не забудьте написать внутреннюю функцию wrapper в is_prime
Функция is_prime должна возвращать wrapper
@is_prime - декоратор для функции sum_three
"""


def is_prime(func):
    def wrapper(*args, **kwargs):
        n = func(*args, **kwargs)
        for i in range(2, int(n/2)+1):
            if n % i == 0:
                print('Простое')
            else:
                print('Составное')
            return n
    return wrapper


@is_prime
def sum_three(a, b, c):
    return a + b + c


result = sum_three(2, 3, 6)
print(result)

