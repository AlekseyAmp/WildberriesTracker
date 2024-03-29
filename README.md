# Отслеживание карточек на площадке Wildberries

Проект предназначен для отслеживания карточек на площадке Wildberries. Включает 4 эндпоинта:

## Swagger
### 0.0.0.0:8000/docs

## Эндпоинты

### POST /add_product
Добавляет продукт.

### GET /get_product/{nm_id}
Получает информацию о продукте по идентификатору.

### GET /get_all_products
Получает информацию о всех продуктах.

### DELETE /delete_product/{nm_id}
Удаляет продукт по идентификатору.

## Запуск проекта
1. Склонируйте репозиторий

   ```bash
   git clone https://github.com/AlekseyAmp/WildberriesTracker.git
2. Создайте файл `.env` в папке `server` и укажите в нем свои данные, используя переменные окружения, представленные в `.env.example`.
3. Создайте файл `alembic.ini` в папке `server/src/adapters/database` и скопируйте в него всё содержащее из `alembic-example.ini`, в sqlalchemy.url указать свои данные.
4. Запустите проект с помощью команды:.

   ```bash
   docker-compose up
## После успешного запуска проекта выполните следующие действия:

### Применение миграций в базу данных

1. Откройте терминал.
2. Выполните команду:

   ```bash
   docker exec -it wbtracker-server bash
3. Перейдите в директорию:

   ```bash
   cd src/adapters/database
3. Выполните следующую команду для применения миграций в базу данных:

   ```bash
   alembic upgrade head
