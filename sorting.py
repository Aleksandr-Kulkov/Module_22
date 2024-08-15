"""Программа получает от пользователя последовательность целых
чисел через пробел, а также любое целое число. Затем:
1. Преобразует введённую последовательность в список;
2. Сортирует элементы списка по возрастанию;
3. Выводит индекс элемента, который меньше введенного пользователем числа,
а следующий за ним больше или равен этому числу;
4. Если введенное число не соответствует заданному условию,
выводит соответствующее сообщение.
"""

try:
    string = input("Введите последовательность целых чисел через пробел: ")
    number = int(input("Введите любое целое число: "))
    list_num = list(map(int, string.split()))
except ValueError:
    print("Введенные данные не соответствуют условию.")
else:
    print("Список чисел: ", list_num)


# Функция сортировки элементов списка по возрастанию (сортировка пузырьком).


    def sort(array):
        for i in range(len(array)):
            for j in range(len(array) - i - 1):
                if array[j] > array[j + 1]:
                    array[j], array[j + 1] = array[j + 1], array[j]
        return array


    sort_list = sort(list_num)
    print("Отсортированный список чисел: ", sort_list)

    if number <= sort_list[0] or number > sort_list[-1]:
        print("Число не соответствует заданному условию.")


# Функция определяет номер позиции элемента, который меньше введенного пользователем числа,
# а следующий за ним больше или равен этому числу (двоичный поиск).


    def binary_search(array, element, left, right):
        if left > right:
            return False

        middle = (left + right) // 2
        if element == array[middle] and array[middle - 1] < element:
            return f"Индекс искомого элемента: {middle - 1}"
        elif element < array[middle] and array[middle - 1] < element:
            return f"Индекс искомого элемента: {middle - 1}"
        elif element == array[middle] and array[middle - 1] == element:
            return binary_search(array, element, left, middle - 1)
        elif element < array[middle] and array[middle - 1] == element:
            return binary_search(array, element, left, middle - 1)
        elif element < array[middle] and array[middle - 1] > element:
            return binary_search(array, element, left, middle - 1)
        elif element > array[middle] and array[middle - 1] < element:
            return binary_search(array, element, middle + 1, right)

    print(binary_search(sort_list, number, 0, len(sort_list)-1))
