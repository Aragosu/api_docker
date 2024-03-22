# Рекомендации по фильмам для пользователей на fastApi
[Ссылка на работающий сервис](https://api-docker-4ked.onrender.com)    
Для просмотра возможностей допишите в адресной строке браузера /docs

## Что есть внутри сервиса?
1. Само приложение на fastapi;
2. БД на postresql;
3. Redis для кэширования результатов выдач (используется для ручек give_rec);
4. pgAdmin если развернуть локально через ```docker compose up --build``` (прикрутил для удобства работы с БД).
   - если вдруг будете запускать проект через докер локально, вход в pgAdmin ```teat_user@gmail.com``` | ```test_12345```


## Структура проекта:
1. docker - файл для запуска приложения;
2. example_pic - скрины для примера функционала;
3. migrations - миграции БД для alembic + заполнение таблиц тестовыми данными;
4. src - основной функционал, включающий:
    - auth - процедуры авторизации и регистрации;
    - ml_model - все что касается работы самой ml-модели (используется lightFM);
    - operations - основной функционал.


## Что умеет делать сервис?
1. Авторизация и регистрация для пользователей - необходимы для разделения существующих и "холодных" пользователей;
![img_auth.png](example_pic/img_auth.png)
2. Основной функционал (поделен на 2 категории существующий/"холодный" пользователь);
![img_main.png](example_pic/img_main.png)    
* ```Give Rec``` - выдает топ-5 фильмов: просто наживаем кнопку - получаем рекомендацию для пользователя;
* ```Give Rec Genre``` - топ-5 фильмов по жанру: тут необходимо ввести жанр на англ (например action);
Если не угадаете с жанром, то вызовется ошибка, перечисляющая доступные жанры.


## Как работаем с функционалом?
#### Первый путь - для авторизованных
1. Заполняем поля username и password (примера можно взять одного из тестовых пользователей: login:test195@mail.com | pass:test);
![img_0_auth_user.png](example_pic/img_0_auth_user.png)
2. После успешного логина можем удостовериться, что зашли в систему вызвав ручку Who Am I;
3. После этого переходим к основному функционалу: ```Give Rec просто```/```Give Rec Genre```.

#### Второй путь - для НЕавторизованных
1. Т.к. мы не авторизованы, то можем сразу перейти к основному функционалу: ```Give Rec``` просто/```Give Rec Genre```;
2. Также есть процедура регистрации пользователя.


## Как запустить проект локально?
0. Написать мне в тг(@aragosu) для получения конфигурационных файлов (если необходимо);
1. Клонируем себе репозиторий на свою машину;
2. Запускаем Docker (или Docker desktop - да, я делал проект на винде **прошу не ругать**);
3. В терминале прописываем ```docker compose up --build```.


## О чем важно упомянуть?
Т.к. хостинг бесплатный (выбирал в учебных целях), то:
1. Первый запуск сервиса (когда переходите по ссылке), может занять некоторое время;
2. Если сервис не получает запросов в течении 50 сек., то он отключается и переводится в состояние описанное в 1п.;
3. Периодически сервис упирается в лимит памяти и может не вызвать ручку.
    - в логах вылетает нечто подобное - ![img.png](example_pic/img_out_of_memory.png)
4. БД доступна до 20.06.2024 (из-за бесплатного хостинга)
