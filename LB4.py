def is_valid_ip(ip):
    parts = ip.split(".")  # Разбиваем строку по точкам
    if len(parts) != 4:  # Проверяем, что частей ровно 4
        return False
    for part in parts:
        if not part.isdigit():  # Проверяем, что часть состоит только из цифр
            return False
        num = int(part)
        if num < 0 or num > 255:  # Проверяем, что число в диапазоне [0, 255]
            return False
    return True

ip_address = input("Введите IP-адрес: ")

if is_valid_ip(ip_address):
    print("YES")
else:
    print("NO")