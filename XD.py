import argparse
import json
from textwrap import indent

# DONE: Читать файл конфига и выводить
# TODO: Открывать файл и менять настройки
# TODO: Написать документацию
# TODO: Написать README

# Чтение конфига
def read_config(filepath):
    with open(filepath, 'r', encoding='utf-8') as f:
        data = json.load(f)
    return(data)

def main():
    # Создаем аргумент парсер
    parser = argparse.ArgumentParser(description="Работа с файлом конфигурации")
    # Создания аргумента для выбора действия    
    parser.add_argument('action',type=str, choices=['read','write','',''])
    # Создание аргумента для имени файла
    parser.add_argument('filepath', type=str)

    # Парсинг агрументов и сохранение в args
    args = parser.parse_args()
    if args.action == 'read':
        config_data = read_config(args.filepath)
        print(json.dump(config_data,indent=3))
    elif args.action == 'write':
        print('write')

if __name__=="__main__":
    main()