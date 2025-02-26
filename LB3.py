                                        #1 variant#
x = input("Введите слово:")
print('*'.join(x))

                                        #2 variant#

input_string = input("Введите строку: ")
# Создаем пустую строку для результата
result = ""

# Проходим по каждому символу в строке
for i in range(len(input_string)):
    # Добавляем текущий символ в результат
    result += input_string[i]
    # Если это не последний символ, добавляем *
    if i != len(input_string) - 1:
        result += "*"

# Вывод результата
print(result)