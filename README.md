## Дипломный проект. Задание 1: Юнит-тесты

### Автотесты для проверки программы, которая помогает заказать бургер в Stellar Burgers

### Реализованные сценарии

Созданы юнит-тесты, покрывающие классы `Bun`, `Burger`, `Ingredient`

Процент покрытия 100% (отчет: `htmlcov/index.html`)

### Структура проекта

- `qa_python_diplom_1` - корневой каталог проекта, содержащий исходный код программы
- `tests`              - пакет, содержащий тесты, разделенные по классам: 
  - `test_bun.py`
  - `test_ingredient.py`
  - `test_burger.py`
  

- `allure_results`     - папка с файлами allure-отчетов о тестировании
- `htmlcov`            - папка с отчетом о покрытии (файл `index.html`)

- `data.py`            - данные и константы для тестов
- `conftest.py`        - фикстуры


- `.gitignore`         - файл для проекта в Git/GinHub
- `requirements.txt`   - файл внешних зависимостей
- `README.md`          - файл с описанием проекта (этот файл)


### Исходные файлы тестируемых классов:
- `bun.py`
- `burger.py`
- `ingredient.py`
- `ingredient_types.py`

### Для запуска тестов должны быть установлены пакеты:
- `pytest`
- `unittest`
- `allure-pytest`
- `allure-python-commons`

### Для генерации отчетов необходимо дополнительно установить пакеты:
- `фреймворк JDK`
- `Allure`
- `pytest-cov`

### Запуск автотестов

**Генерация файла зависимостей**

> `$ pip freeze > requirements.txt`

**Установка зависимостей**

> `$ pip install -r requirements.txt`

**Запуск всех тестов выполняется командой**

>  `$ pytest -v ./tests`

**Запуск автотестов и создание HTML-отчета о покрытии**

>  `$ pytest --cov --cov-branch --cov-report=html`

**Запуск автотестов с генерацией отчета Allure**

>  `$ pytest -v ./tests  --alluredir=allure_results`

**Просмотр отчета Allure**

>  `$ allure serve allure_results`
