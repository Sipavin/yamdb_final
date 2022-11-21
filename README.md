# YaMDb

![YaMDb workflow](https://github.com/sipavin/yamdb_final/actions/workflows/yamdb_workflow.yml/badge.svg)

# api_yamdb

### О проекте

Данный проект является учебным.
Проект YaMDb собирает отзывы (Review) пользователей на произведения (Titles). Произведения делятся на категории (Category): «Книги», «Фильмы», «Музыка».
Сами произведения в YaMDb не хранятся.
Произведению может быть присвоен жанр (Genre).
Пользователи YaMDb оставляют к произведениям текстовые отзывы (Review) и ставят произведению оценку в диапазоне от одного до десяти (целое число); из пользовательских оценок формируется усреднённая оценка произведения — рейтинг (целое число).

### Как запустить проект.

Убедитесь, что в вашей системе установлен и запущен Docker

Клонируйте репозиторий и перейдите в него в командной строке:

```
git clone https://github.com/sipavin/infra_sp2.git
```

```
cd infra_sp2/infra
```

Соберите и запустите контейнеры:

```
docker-compose up -d --build
```

Выполните миграции:
```
docker-compose exec web python manage.py migrate
```

Создайте суперпользователя:

```
docker-compose exec web python manage.py createsuperuser
```

Обработайте статику:

```
docker-compose exec web python manage.py collectstatic --no-input
```

Ваш проект готов к работе по адресу http://localhost/admin/


### Шаблон наполнения env-файла:

- указывается, что работаем с postgresql:

DB_ENGINE=django.db.backends.postgresql

- задается имя базы данных:

DB_NAME=postgres

- задается логин для подключения к базе данных:

POSTGRES_USER=login(установите свой)

- задается пароль для подключения к БД

POSTGRES_PASSWORD=password(установите свой)

- задается название сервиса (контейнера)

DB_HOST=db

- задается порт для подключения к БД

DB_PORT=5432

- задается Secret Key Django

SECRET_KEY=secret_key(установите свой)


### Как создать резервную копию базы данных:

Введите команду:

```
docker-compose exec web python manage.py dumpdata > fixtures.json
```

Резервная копия базы данных будет сохранена в файле fixtures.json
каталога infra_sp2/infra

### Как заполнить базу начальными данными:

Копируем файл с данными fixtures.json в контейнер web:

```
docker cp ../infra/fixtures.json <CONTAINER_ID>:/app
```

Заходим в контейнер:

```
docker exec -it <CONTAINER_ID> bash
```

Выполняем команды:

```
python3 manage.py shell  
# в открывшемся SHELL выполняем:
>>> from django.contrib.contenttypes.models import ContentType
>>> ContentType.objects.all().delete()
>>> quit()

python manage.py loaddata fixtures.json 
```

Данные загружены

### Как делать запросы:

К проекту по адресу http://51.250.30.226/redoc/ подключена документация redoc, содержащая сведения по доступным эндпоинтам и примеры запросов.
