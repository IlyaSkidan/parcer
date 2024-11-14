import re

# Замените этот адрес на ваш MAC-адрес
mac_address = "your_mac_address"

# Путь к вашему .dat файлу
file_path = 'your_path'

# Читаем содержимое файла
with open(file_path, 'r') as file:
    content = file.read()

# Заменяем все вхождения HOSTID=XXXXXXXXX на HOSTID=MAC_ADDRESS
new_content = re.sub(r'HOSTID=xxxxxxxxxxxx', f'HOSTID={mac_address}', content)

# Записываем измененное содержимое обратно в файл
with open(file_path, 'w') as file:
    file.write(new_content)

print("Замена завершена!")
