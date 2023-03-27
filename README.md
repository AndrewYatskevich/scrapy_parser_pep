# scrapy_parser_pep

### Описание

Парсер документации PEP с возможностью сохранением в файл.

### Технологии

Python 3.7
Scrapy 2.5.1

### Запуск проекта в dev-режиме

- Клонировать репозиторий и перейти в него в командной строке:

```
git clone https://github.com/AndrewYatskevich/scrapy_parser_pep.git
```

```
cd scrapy_parser_pep
```

- Cоздать и активировать виртуальное окружение:

```
python3 -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

- Установить зависимости из файла requirements.txt:

```
python3 -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

- Запустить проект:

```
scrapy crawl pep
```

Автор: Андрей Яцкевич https://github.com/AndrewYatskevich
