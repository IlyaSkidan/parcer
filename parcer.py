import re

# Замените этот адрес на ваш MAC-адрес
mac_address = "50ebf692cc03 , 00155d020c11 , 0a002700000c , 161333693da1 , 161333693db1 , 141333693db1 , 00155d4c9a9d"

# Путь к вашему .dat файлу
file_path = 'C:/Users/Илья/Downloads/License_new.dat'

# Читаем содержимое файла
with open(file_path, 'r') as file:
    content = file.read()

# Заменяем все вхождения HOSTID=XXXXXXXXX на HOSTID=MAC_ADDRESS
new_content = re.sub(r'HOSTID=xxxxxxxxxxxx', f'HOSTID={mac_address}', content)

# Записываем измененное содержимое обратно в файл
with open(file_path, 'w') as file:
    file.write(new_content)

print("Замена завершена!")
