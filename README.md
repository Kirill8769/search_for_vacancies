# Поиск вакансий

Это простая консольная программа для поиска вакансий с использованием API HeadHunter и SuperJob. Программа взаимодействует с пользователем, предоставляя выбор источников данных и ключевого запроса для поиска вакансий. Результаты сохраняются в JSON-файл для дальнейшего использования.

## Установка и запуск

### Склонируйте репозиторий:
```bash
git clone https://github.com/Kirill8769/search_for_vacancies.git
```
### Перейдите в папку с проектом
```bash
cd search_for_vacancies
```
### Установите зависимости:
Сначала активируем poetry
```bash
poetry shell
```
Затем установим все зависимости из pyproject.toml
```bash
poetry install
```
### Запустите программу:

```bash
python src\main.py
```
## Использование

    При запуске программы вы увидите приветствие и меню выбора источников данных.

    Введите номер источника данных (1 - HeadHunter, 2 - SuperJob, 3 - оба).

    Введите ключевой запрос для поиска вакансий.

    Результаты поиска будут сохранены в JSON-файле с именем, содержащим запрос.

    Выберите дополнительную утилиту:
        1 - Вывести топ-10 вакансий.
        2 - Вывести топ-10 вакансий с сортировкой по дате.
        3 - Вывести все вакансии с сортировкой по дате.
        4 - Выйти из программы.

## Примечание

Для работы с SuperJob API необходимо иметь свой собственный токен, который нужно указать в переменной окружения.
Результаты поиска сохраняются в файл в формате JSON для последующего использования и анализа.

## Лицензия

Этот проект распространяется под лицензией MIT. Вся информация о вакансиях предоставляется соответствующими API HeadHunter и SuperJob.