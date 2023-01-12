![PyDonSys preview](https://raw.githubusercontent.com/wezzyofficial/pydonsys/main/assets/screen1.jpg)

## _PyDonSys - система для онлайн приёма донатов на QIWI написанная на Python и работает на Django._

Проект поставляется как есть. И был написан меньше чем за 24 часа! Будет время и желание - буду поддерживать.


## Установка

PyDonSys работает на [Django](https://www.djangoproject.com/) 4+.

Для начала установите зависимости для запуска проекта:

```sh
pip install requirements.txt
```

> Измените подключение к базе данных, если планируете использовать другую базу - [тык](https://docs.djangoproject.com/en/4.1/ref/databases/).
> Если же нет, то можем просто запустить базу данных в Docker, через docker-compose.

Для запуска базы данных в Docker, через docker-compose:
```sh
docker-compose up -d
```

Далее нам необходимо провести применить миграции базы данных:

```sh
python manage.py makemigrations
python manage.py migrate
```

Создаём нового пользователя для Админ-панели:

```sh
python manage.py createsuperuser
```

И проводим первоначальную настройку:

```sh
python manage.py fs
```

Ну и запускаем на проект:
```sh
python manage.py runserver
```

> Перед развертываем проекта в prod, не забываем выключить DEBUG мод в настройках проекта.

> URL для доступа к админке изменён со стандартного, на /ybXvz5S3wzR0