"""Задача3
"""

import math

# заданная плотность распределения
def normal_pdf(x):
    return (1 / (4 * math.sqrt(2 * math.pi))) * math.exp(-(x + 2)**2 / 32)

# нахождение математического ожидания
def mean():
    return -2

# нахождение дисперсии
def variance():
    return 32

# нахождение среднего квадратичного отклонения
def std():
    return math.sqrt(variance())

# вывод результатов
print("Математическое ожидание: ", mean())
print("Дисперсия: ", variance())
print("Среднее квадратичное отклонение: ", std())
