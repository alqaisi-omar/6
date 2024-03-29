# Вариант 6
print("1. Дан одномерный массив из 10 целых чисел. Найти максимальный элемент и сравнить с ним остальные элементы. Вывести количество меньших максимального и больших максимального элемента.")
array = [int(input(f"Введите {i + 1}-й элемент: ")) for i in range(10)]

# Находим максимальный элемент
max_element = max(array)

# Считаем количество элементов, меньших и больших максимального
count_less = sum(1 for num in array if num < max_element)
count_greater = sum(1 for num in array if num > max_element)

print("Количество элементов меньше максимального:", count_less)
print("Количество элементов больше максимального:", count_greater)

print("\n2. Одномерный массив из 10-и целых чисел заполнить с клавиатуры, определить сумму тех чисел, которые >5.")
array = [int(input(f"Введите {i + 1}-й элемент: ")) for i in range(10)]

# Считаем сумму элементов, больших 5
sum_greater_than_5 = sum(num for num in array if num > 5)

print("Сумма элементов, которые больше 5:", sum_greater_than_5)
