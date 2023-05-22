# YaCut сервис укорачивания ссылок

## Описание

Cервис укорачивает ссылки. Его назначение — ассоциировать длинную пользовательскую ссылку с короткой, которую предлагает сам пользователь или предоставляет сервис.  

## Стек технологий:

```
Python 3.7  
Flask 2.0.2
```

## Как запустить проект:
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

source venv/scripts/activate
```

Установить зависимости из файла requirements.txt:

```
python -m pip install --upgrade pip

pip install -r requirements.txt
```

Создать и применить миграции:

```
flask db init

flask db migrate

flask db upgrade
```
Запустить сервис:
```
flask run
```
