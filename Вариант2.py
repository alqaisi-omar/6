# Вариант 2
print("1. Дан одномерный массив, состоящий из N целочисленных элементов. Ввести массив с клавиатуры. Найти минимальный элемент. Вывести индекс минимального элемента на экран.")
n = int(input("Введите длину массива: "))
array = []

# Ввод массива
for i in range(n):
    array.append(int(input(f"Введите {i + 1}-й элемент: ")))

# Находим минимальный элемент и его индекс
min_element = min(array)
min_index = array.index(min_element)

print("Минимальный элемент:", min_element)
print("Индекс минимального элемента:", min_index)

print("\n2. Дан массив целых чисел. Переписать все положительные элементы во второй массив, а остальные - в третий.")
positive_array = []
negative_array = []

# Разделение элементов на положительные и отрицательные
for num in array:
    if num > 0:
        positive_array.append(num)
    else:
        negative_array.append(num)

print("Положительные элементы:", positive_array)
print("Отрицательные элементы:", negative_array)
