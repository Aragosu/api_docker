## Продвинутое использование FastAPI

### Роутеры, запросы к базе данных через ORM, файловая структура, обработка ошибок.
1. https://fastapi.tiangolo.com/tutorial/bigger-applications/
2. https://github.com/zhanymkanov/fastapi-best-practices – внутри src разбиение по сервисам
3. Создаем папку operations. Пишем в models.py
4. Смотрим в env.py на импорты, потом на asyncpg и async_fallback
5. Перенос рута в src и invalidate cache (в PyCharm)
6. Смотрим на router в operations. Роутер нужен когда приложение большое и мы хотим разделить функции. 
Главный роутер – app. Мы можем создавать отдельные APIRouter, импортируем эти эндпойнты в main.py.
7. ORM - object-relational model. relation - таблица, object - что-то в ЯП
8. SQL injection - если будем посылать сырые запросы то надо быть супераккуратным
9. Запускает код не sqlalchemy (лишь конструирует запросы), а драйвер
10. query - запросы на get, stmt - statement
11. Создаем схему pydantic
12. Делаем get и post, убираем Z для таймзоны в дате при тестировании
13. await session.commit() – без commit не будет применен модифицируюший запрос
14. Зачем в models есть Table и Class User? - императивный и декларативный подходы. 
Класс заставляет нас использовать библиотека fastapi users
15. Пробуем получить ошибки – столбец types в get, в operation_type int поставить. 5хх скрываем, 4хх нет


Источник: https://github.com/artemonsh/fastapi_course