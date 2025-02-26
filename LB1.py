def sum_with_for(numbers):
    total = 0
    for num in numbers:
        total += num
    return total
def sum_with_while(numbers):
    total = 0
    i = 0
    while i < len(numbers):
        total += numbers[i]
        i += 1
    return total
def sum_with_recursion(numbers):
    if not numbers:  # Возвращаем 0
        return 0
    return numbers[0] + sum_with_recursion(numbers[1:])  # делаем рекурсию

numbers = [1, 2, 3, 4, 5]

# Вызов функций и вывод результатов
print("Сумма с for:", sum_with_for(numbers))
print("Сумма с while:", sum_with_while(numbers))
print("Сумма с рекурсией:", sum_with_recursion(numbers))