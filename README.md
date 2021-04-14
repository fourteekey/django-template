#Django-Template 
``
Пустой шаблон для проекта джанго с конфигурационными файлами.
Инструкция на Notion.
``
 
### Настройки
```
$ pip install -r requirements
$ cp config/example.env config/.env
$ python manage.py makemigrations
$ python manage.py migrate
```

### Настройки на деплое
```
$ cd /.systemfilte | sudo cp -rp etc /etc/
```

### Запуск бэкенда

```
$ python manage.py runserver
```
