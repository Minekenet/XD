# Изменение конфига
## Описание
Данная программа имеет функционал для чтения и редактирования параметров в вашем ```config``` файле
## Как запустить
Команда для вызова справки
```powershell
python XD.py -h 
```
## Содержание
В вашем каталоге должен находится 
* `config.json` - Файл с вашими настройками 
* `XD.py` - Файл с кодом для изменения настроек или чтения конфига  

### Функции XD.py
```python
def main()
```
- Основная функция в которой мы:

1) Создаем парсер аргуменотов 
2) Создаем аргумент для имени файла. Он принимает путь до файла для функции ```read_config```
3) Cоздаем аргумент для параметра и его нового значения 
3) Парсер аругментов и сохранение их в переменую ```args```
4) Проверка выбора аргумента и дальнейший запуск действий 
 
```python
def read_config()
```
- Функция чтения конфига >> Принимает имя файлы/Возвращает его содержимое

```python
def write_config()
```
- Функция записи конфига в файл >> Принимает имя, содержимое файла/Ничего не возвращает 
```python
def update_config()
```
- Функция изменения параметра в конфиге >> Принимает содержимое файла, свойство, значение для свойства/Ничего не возвращает

## Примеры использования
- Пример Конфига
```java
{
    "server": {
        "host": "192.126.5.4",
        "port": 8080,
        "debug": "false"
    }
}
```
- Цель: Изменить значение ```"port"``` на ```2000```

1) Вводим команду

``` 
python XD.py write config.json --param server.host=192.126.5.4
```
Где ```XD.py``` - Имя файла с кодом,

```write``` - аргумент для редактирования файла

```config.json``` - название вашего файла с конфигурацией


## Испольуемые модули
```python
1) import argparse
2) import json 
```
Модуль `argparse` позволяет легко писать удобную для пользователя командную строку интерфейсы. Программа определяет, какие аргументы ей требуются. Модуль также автоматически генерирует справочные сообщения и сообщения об использовании. Модуль также будет выдавать ошибки, когда пользователи предоставляют программе неверные аргументы.
- Подробная документация по [argparse](https://docs.python.org/3/library/argparse.html)

Модуль `json` нужен для для работы с форматом .json для чтения и записи в файл
- Подробная документация по [json](https://docs.python.org/3/library/json.html)

## Автор
- [Minekenet](https://github.com/Minekenet)