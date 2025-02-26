def count_characters(s):
    # Создаем пустой словарь для хранения количества вхождений символов
    char_count = {}
    # Гуляем по каждому символу в строке
    for char in s:
        # Если символ есть в словаре, увеличиваем его счетчик
        if char in char_count:
            char_count[char] += 1
        # Если символа нет в словаре, добавляем его с значением 1
        else:
            char_count[char] = 1
    return char_count

input_string = input("Введите строку: ")
# Подсчет количества вхождений символов
result = count_characters(input_string)
print("Количество вхождений каждого символа:")
for char, count in result.items():
    print(f"'{char}': {count}")