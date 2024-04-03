# Дипломная работа к профессии Python-разработчик «API Сервис заказа товаров для розничных сетей».

## Общее описание приложения

Приложение предназначено для автоматизации закупок в розничной сети через REST API.

**Пользователи сервиса:**

1. Клиент (покупатель):

- делает ежедневные закупки по каталогу, в котором представлены товары от нескольких поставщиков,
- в одном заказе можно указать товары от разных поставщиков,
- пользователь может авторизироваться, регистрироваться и восстанавливать пароль через API.
    
2. Поставщик:

- через API информирует сервис об обновлении прайса,
- может включать и отключать приём заказов,
- может получать список оформленных заказов (с товарами из его прайса).

### Для запуска проекта необходимо:

Установить зависимости:

```bash
pip install -r requirements.txt
```

Создать базу, осуществить миграции, создать суперпользователя:

```bash
manage.py makemigrations
manage.py migrate
manage.py createsuperuser
```

Проверить работу модулей:

```bash
python manage.py runserver
```
    
### Развертывание проекта с помощью docker-compose :

```bash
docker-compose build
docker-compose up -d
```   
Подсказки:

[Как установить Docker на Ubuntu](https://help.reg.ru/support/servery-vps/oblachnyye-servery/ustanovka-programmnogo-obespecheniya/kak-ustanovit-docker-na-ubuntu?query=%d0%ba%d0%b0%d0%ba%20%d1%83%d1%81%d1%82%d0%b0%d0%bd%d0%be%d0%b2%d0%b8%d1%82%d1%8c%20docker)

[Как установить и настроить Redis на Linux](https://help.reg.ru/support/servery-vps/oblachnyye-servery/ustanovka-programmnogo-obespecheniya/kak-ustanovit-i-nastroit-redis-na-linux)

[Flower](https://flower.readthedocs.io/en/latest/)

### Тестирование проекта:

```bash
python manage.py test
```

### Проверка покрытия проекта тестами:

```bash
pytest --cov=backend
```
 ### Реализованы на базовом уровне:

- Автогенерация документации Open API в рамках пакета DRF-Spectacular
- Авторизация (ВКонтакте) с помощью библиотеки social-app-django
- Мониторинг с помощью Sentry
- С помощью пакета django-silk можно анализировать запросы к БД
- Изменение админки с помощью библиотеки django-jet-reboot
- Добавление миниатюр товаров с помощью библиотеки easy-thumbnails
- DRF тротлинг