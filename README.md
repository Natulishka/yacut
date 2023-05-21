Клонировать репозиторий и перейти в него в командной строке:

```
git@github.com:Natulishka/yacut.git
```

```
cd yacut
```

Cоздать и активировать виртуальное окружение:

```
python -m venv venv
```

* Если у вас Linux/macOS

    ```
    source venv/bin/activate
    ```

* Если у вас windows

    ```
    source venv/scripts/activate
    ```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip
```

```
pip install -r requirements.txt
```

Создать и применить миграции:

```
flask db init

flask db migrate

flask db upgrade
```
