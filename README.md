# YADRO Lab Test Task

Тестовое задание для проекта "Система проверки работоспособности дистрибутивов на основе Yocto".

## Краткое описание

Система автоматического тестирования веб-сервера Apache при помощи pytest и Allure.
Система тестирования (`agent`) содержит ряд тестов для проверки работоспособности и корректности работы сервера apache2 (`target`), а так же набор смоук-тестов для проверки работоспособности пакетов tar и ln. Результаты тестов собираются в отчёт при помощи Allure.
`agent` и `target` запускаются в отдельных докер-контейнерах, соёдинённых через SSH, и конфигурируется при помощи Docker Compose.

## Необходимые требования и зависимости зависимости

- `Docker`
- `Docker Compose v2`
- Браузер для просмотра отчёта Allure

## Сборка и запуск проекта

Сначала соберите docker-образы для `agent` и `target`:
```bash
docker compose build
```
Вы можете конфигурировать данные для подключения `agent` к `target` в файле `.example.env` и скопировав его в содержимое в файл `.env`:
```bash
cp .example.env .env
```

Чтобы запустить всю систему и выполнить тесты, используйте следующую команду:
```bash
docker compose up --abort-on-container-exit
```
Чтобы остановить контейнеры и очистить папки с данными Allure, выполните команду:
```bash
docker compose down && rm -rf allure-report allure-results
```

## Ожидаемый результат

После запуска в консоли будет отображен вывод логов обоих контейнеров. В логах контейнера `agent` вы увидите подробный отчет о результатах Pytest, который будет выглядеть примерно так:
```bash
============================= test session starts ==============================
platform linux -- Python 3.11.2, pytest-8.4.2, pluggy-1.6.0
rootdir: /app
plugins: allure-pytest-2.15.0
collected 6 items

tests/test_apache_404_page.py .                                          [ 16%]
tests/test_apache_errors_in_logs.py .                                    [ 33%]
tests/test_apache_index_page.py .                                        [ 50%]
tests/test_apache_service_running.py .                                   [ 66%]
tests/test_smoke_tar.py .                                                [ 83%]
tests/test_smole_ln.py .                                                 [100%]

============================== 6 passed in 0.77s ===============================
Report successfully generated to /app/allure-report
```

## Просмотр отчёта Allure

Для просмотра отчёта Allure в браузере перейдите по адресу http://localhost:8080. Отчёт должен иметь следующий вид:
<img width="949" height="708" alt="image" src="https://github.com/user-attachments/assets/9eb4baf6-dd3f-44d1-aec4-d3f5be89be48" />
<img width="949" height="708" alt="image" src="https://github.com/user-attachments/assets/f420f411-5e12-4be0-9990-ebf892f39598" />


