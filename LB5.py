def is_palindrome(s):
    # Удаляем все небуквенные символы и приводим к нижнему регистру
    cleaned = ''.join(char.lower() for char in s if char.isalpha())
    # Проверяем, является ли строка палиндромом
    return cleaned == cleaned[::-1]

# Ввод строки от пользователя
input_string = input("Введите строку: ")

# Проверка и вывод результата
if is_palindrome(input_string):
    print("YES")
else:
    print("NO")