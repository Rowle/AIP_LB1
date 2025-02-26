def separate_negatives(numbers):
    insert_pos = 0
    # Проходим по списку
    for i in range(len(numbers)):
        if numbers[i] < 0:
            # Если текущий отрицательный, меняем его местами с элементом на позиции
            numbers[i], numbers[insert_pos] = numbers[insert_pos], numbers[i]
            # Увеличиваем позицию
            insert_pos += 1
    return numbers

import random
# Рандом список
random_numbers = [random.randint(-10, 10) for _ in range(10)]
print("Исходный список:", random_numbers)
# Юзаем функцию
separated_numbers = separate_negatives(random_numbers)
print("Список после разделения:", separated_numbers)