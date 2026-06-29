# Cash Flow Management

Тестовое задание на Django.

## Стек

- Python 3.13
- Django 6
- SQLite3
- django-filter
- Bootstrap 5

## Установка

```bash
git clone <repository_url>

cd Cash_flow

python -m venv venv
```

Windows

```bash
venv\Scripts\activate
```

Linux/macOS

```bash
source venv/bin/activate
```

Установить зависимости

```bash
pip install -r requirements.txt
```

Выполнить миграции

```bash
python manage.py migrate
```

Создать администратора

```bash
python manage.py createsuperuser
```

Запустить сервер

```bash
python manage.py runserver
```

После запуска приложение будет доступно по адресу

```
http://127.0.0.1:8000/
```

Административная панель

```
http://127.0.0.1:8000/admin/
```

## Возможности

- CRUD операций
- Фильтрация
- Валидация бизнес-логики
- Зависимые категории и подкатегории (AJAX)
- Административная панель
- SQLite (создается автоматически после миграций)
