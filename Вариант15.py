# Вариант 15
print("1. Определите, есть ли в списке повторяющиеся элементы, если да, то вывести на экран эти значения.")
array = [int(input(f"Введите {i + 1}-й элемент: ")) for i in range(10)]

# Проверяем наличие повторяющихся элементов
duplicates = set()
found_duplicates = False
for num in array:
    if array.count(num) > 1:
        duplicates.add(num)
        found_duplicates = True

if found_duplicates:
    print("Найдены повторяющиеся элементы:", duplicates)
else:
    print("Повторяющихся элементов нет.")

print("\n2. Дан одномерный массив целого типа. Получить другой массив, состоящий только из нечетных чисел исходного массива или сообщить, что таких чисел нет. Полученный массив вывести в порядке убывания элементов.")

# Ввод массива
array = [int(input(f"Введите {i + 1}-й элемент: ")) for i in range(10)]

# Фильтруем только нечетные числа
odd_numbers = [num for num in array if num % 2 != 0]

if odd_numbers:
    odd_numbers.sort(reverse=True)
    print("Массив из нечетных чисел в порядке убывания:", odd_numbers)
else:
    print("В исходном массиве нет нечетных чисел.")
