"""
Домашнее задание №1
Функции и структуры данных
"""
def power_numbers(*numbers):

    """
    функция, которая принимает N целых чисел,
    и возвращает список квадратов этих чисел
    >>> power_numbers(1, 2, 5, 7)
    <<< [1, 4, 25, 49]
    """
    for number in numbers:
        return [number ** 2 for number in numbers]

power_numbers()

# filter types
ODD = "odd"
EVEN = "even"
PRIME = "prime"

def is_prime(number):
    if number <= 1:
        return False
    for i in range(2, number):
        if number % i == 0:
            return False
        else:
            return True

def filter_numbers(number_list, filter_type):
    """
    функция, которая на вход принимает список из целых чисел,
    и возвращает только чётные/нечётные/простые числа
    (выбор производится передачей дополнительного аргумента)

    >>> filter_numbers([1, 2, 3], ODD)
    <<< [1, 3]
    >>> filter_numbers([2, 3, 4, 5], EVEN)
    <<< [2, 4]
    >>> filter_numbers([1, 2, 3, 4, 5, 6, 7, 8, 11], PRIME)
    <<< [2, 3, 5, 7, 11]
    """
    if filter_type == ODD:
        return [number for number in number_list if number % 2 != 0]

    if filter_type == EVEN:
        return [number for number in number_list if number % 2 == 0]

    if filter_type == PRIME:
        return list(filter(is_prime, number_list))




