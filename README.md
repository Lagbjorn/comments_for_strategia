# Тестовое задание для Strategia
Задание: Реализовать REST API для системы комментариев блога.
------
Функциональные требования:
У системы должны быть методы API, которые обеспечивают
- Добавление статьи (Можно чисто номинально, как сущность, к которой крепятся комментарии).
- Добавление комментария к статье.
- Добавление коментария в ответ на другой комментарий (возможна любая вложенность).
- Получение всех комментариев к статье вплоть до 3 уровня вложенности.
- Получение всех вложенных комментариев для комментария 3 уровня.
- По ответу API комментариев можно воссоздать древовидную структуру.

Нефункциональные требования:
- Использование Django ORM.
- Следование принципам REST.
- Число запросов к базе данных не должно напрямую зависеть от количества комментариев, уровня вложенности.
- Решение в виде репозитория на Github, Gitlab или Bitbucket.
- readme, в котором указано, как собирать и запускать проект. Зависимости указать в requirements.txt либо использовать poetry/pipenv.
- Использование свежих версий python и Django.

Будет плюсом:
- Использование PostgreSQL.
- docker-compose для запуска api и базы данных.
- Swagger либо иная документация к апи.

## Описание реализации
Документация API описана в формате Swagger/OpenAPI и лежит в `comments_for_strategia/docs/api.yml`.

В задании не требовалось реализовать production-среду, поэтому я настроил только dev-среду.

Для реализации дерева комментариев структура данных MPTT, а именно пакет `django-mptt`.

Для удобства отладки в dev-среде используется `django-debug-toolbar`. Кроме того, в логах пишется список запросов к БД.
Благодаря этому вы можете убедиться, что получение дерева комментариев требует лишь два запроса к базе,
независимо от их количества и уровня вложенности.

Добавление комментария дороже с точки зрения количества запросов: 3 запроса для комментария нулевой вложенности
и 5 для добавления комментария любой другой вложенности из-за необходимости перестроения MPTT в базе данных.

## Сборка и запуск
Для удобства, приложение запускается в Docker.
В `example-secrets.env` перечислены переменные среды, требуемые для запуска контейнеров.
Создайте свой файл со своими секретами, или просто используйте пример :)

При запуске контейнера автоматически подгрузится фикстура с начальными данными 
в виде статьи и пяти комментариев к ней.

```commandline
docker compose --env-file <your-env-file> up --build
```
