def binary_search(array, element, left, right):

    middle = (left + right) // 2

    if array[left] >= element:
        return "Нет чисел соответсвующих условию"

    if array[middle] < element and array[middle+1] >= element:
        return middle
    elif element >= middle:
        return binary_search(array, element, left, middle - 1)
    else:
        return binary_search(array, element, middle + 1, right)
      
a = input("Введите последовательность чисел через пробел ").split()
element = int(input('Введите число '))
array = sorted(list(map(int, a)))

print(binary_search(array, element, 0, len(array) - 1))
print(array)
