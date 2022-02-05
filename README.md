# Старт

## 1. В корне проекта создать .env и прописать свои настройки

#### SECRET_KEY = ''
#### DEBUG = True
#### ALLOWED_HOSTS = *
#### DB_ENGINE = django.db.backends.postgresql_psycopg2
#### DB_NAME = pgdb
#### DB_USER = postgres
#### DB_PASSWORD = postgres
#### DB_HOST = 127.0.0.1
#### DB_PORT = 5432

# 2. Создать образ и запустить контейнер

#### docker-compose up --build
