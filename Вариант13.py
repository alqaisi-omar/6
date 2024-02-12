# Вариант 13
print("1. Дан одномерный массив целых чисел. Проверить, есть ли в нем одинаковые элементы. Вывести эти элементы и их индексы.")
array = [int(input(f"Введите {i + 1}-й элемент: ")) for i in range(10)]

# Проверяем наличие одинаковых элементов
duplicates = {}
for i in range(len(array)):
    if array[i] in duplicates:
        duplicates[array[i]].append(i)
    else:
        duplicates[array[i]] = [i]

found_duplicates = False
for num, indices in duplicates.items():
    if len(indices) > 1:
        print(f"Элемент {num} повторяется в позициях:", indices)
        found_duplicates = True

if not found_duplicates:
    print("Одинаковых элементов нет.")

print("\n2. Дан одномерный массив из 8 элементов. Заменить все элементы массива")

# Ввод массива
array = [int(input(f"Введите {i + 1}-й элемент: ")) for i in range(8)]

# Заменяем все элементы массива
for i in range(len(array)):
    array[i] = 0 if array[i] < 0 else array[i]

print("Преобразованный массив:", array)
