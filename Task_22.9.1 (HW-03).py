while True:
    try:
        sequence = input("Введите последовательность чисел через пробел: ")
        array_str = sequence.split()
        array_int = [int(x) for x in array_str]
        break
    except:
        print("Ошибка, повторите ввод!")

while True:
    try:
        value = int(input("Введите любое число: "))
        if type(value) == int:
            break
    except:
        print("Ошибка, повторите ввод!")

for i in range(len(array_int)):
    for j in range(len(array_int) - i - 1):
        if array_int[j] > array_int[j + 1]:
            array_int[j], array_int[j + 1] = array_int[j + 1], array_int[j]

print(array_int)

from bisect import bisect_left
def binary_search(array_int, value):
    position_num = bisect_left(array_int, value)
    if position_num <= len(array_int):
        return position_num -1

print(binary_search(array_int, value))