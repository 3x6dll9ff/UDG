def factorial(n):
    if n == 0:  # Базовый случай: факториал 0 равен 1
        return 1
    else:
        return n * factorial(n - 1)  # Рекурсивный случай: n * (n-1)!
    
# # Пример
# print(factorial(5))  # 120

# def fibonacci(n):
#     if n == 0:  # Базовый случай для n = 0
#         return 0
#     elif n == 1:  # Базовый случай для n = 1
#         return 1
#     else:
#         return fibonacci(n - 1) + fibonacci(n - 2)  # Рекурсивный случай: сумма двух предыдущих чисел
    
# # Пример
# print(fibonacci(7))  # 13


# def sum_list(lst):
#     if len(lst) == 0:  # Базовый случай: если список пуст, вернуть 0
#         return 0
#     else:
#         return lst[0] + sum_list(lst[1:])  # Рекурсивный случай: первый элемент + сумма оставшихся элементов
    
# # Пример
# print(sum_list([1, 2, 3, 4, 5]))  # 15

def reverse_string(s):
    if len(s) == 0:  # Базовый случай: если строка пустая, вернуть пустую строку
        return s
    else:
        return reverse_string(s[1:]) + s[0]  # Рекурсивный случай: разворачиваем подстроку и добавляем первый символ
    
# Пример
print(reverse_string("hello"))  # "olleh"


def find_max(lst):
    if len(lst) == 1:  # Базовый случай: если в списке один элемент, он и есть максимальный
        return lst[0]
    else:
        max_of_rest = find_max(lst[1:])  # Рекурсивный случай: находим максимум оставшихся элементов
        return max(lst[0], max_of_rest)  # Возвращаем максимум между первым элементом и остальными
    
# Пример
print(find_max([3, 1, 4, 1, 5, 9, 2, 6]))  # 9

