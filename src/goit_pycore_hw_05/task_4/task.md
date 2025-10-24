# Task 4

Розробіть Python-скрипт для аналізу файлів логів.
Скрипт повинен вміти читати лог-файл, переданий як аргумент командного рядка,

## Вимоги до завдання:

1. Всі помилки введення користувача повинні оброблятися за допомогою декоратора `input_error`. Цей декоратор відповідає за
   повернення користувачеві повідомлень типу `"Enter user name"`, `"Give me name and phone please"` тощо.
2. Декоратор input_error повинен обробляти винятки, що виникають у функціях - `handler` і це винятки: `KeyError`,
   `ValueError`, `IndexError`. Коли відбувається виняток, декоратор повинен повертати відповідну відповідь користувачеві.
   Виконання програми при цьому не припиняється.

## Рекомендації для виконання:

В якості прикладу додамо декоратор input_error для обробки помилки `ValueError`

```python
def input_error(func):
    def inner(*args, **kwargs):
        try:
            return func(*args, **kwargs)
        except ValueError:
            return "Give me name and phone please."

    return inner
```

Та обгорнемо декоратором функцію `add_contact` нашого бота, щоб ми почали обробляти помилку `ValueError`.

```python
@input_error
def add_contact(args, contacts):
    name, phone = args
    contacts[name] = phone
    return "Contact added."
```

Вам треба додати обробники до інших команд (функцій), та додати в декоратор обробку винятків інших типів з відповідними повідомленнями.

## Критерії оцінювання:

1. Наявність декоратора `input_error`, який обробляє помилки введення користувача для всіх команд.
2. Обробка помилок типу `KeyError`, `ValueError`, `IndexError` у функціях за допомогою декоратора `input_error`.
3. Кожна функція для обробки команд має декоратор `input_error`, який обробляє відповідні помилки і повертає відповідні повідомлення про помилку.
4. Коректна реакція бота на різні команди та обробка помилок введення без завершення програми.

## Приклад використання:

При запуску скрипту діалог з ботом повинен бути схожим на цей.

```text
Enter a command: add
Enter the argument for the command
Enter a command: add Bob
Enter the argument for the command
Enter a command: add Jime 0501234356
Contact added.
Enter a command: phone
Enter the argument for the command
Enter a command: all
Jime: 0501234356
Enter a command:
```
