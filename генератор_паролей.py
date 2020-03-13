import string
import random
from typing import List

def generate_random_string(length: int, *choices: str) -> str:
    """
    Generate a string of a given `length`.

    The result has at least one symbol from each of `choices` if `length` allows.

    Arguments:
        length -- Result string length.
        choices -- Strings with available symbols.
    """
    if not choices:
        # будем использовать только буквы если нам все равно, из каких символов пароль
        choices = (string.ascii_letters, ) 

    # создадим строку со всеми доступными символами
    all_choices = "".join(choices)
    result: List[str] = []
    choice_index = 0
    while len(result) < length:
        # получим по символу из каждого списка, чтобы
        # каждый список был использован хотя бы один раз
        if choice_index < len(choices):
            symbol = random.choice(choices[choice_index])
            result.append(symbol)
            choice_index += 1
            continue

        # а после этого добавляем символы из любого списка
        symbol = random.choice(all_choices)
        result.append(symbol)

    # перемешаем наш результат чтобы распределить начальные символы
    random.shuffle(result)
    return "".join(result)

def generate_mydb_password(length: int) -> str:
    """
    Generate a random password for MyDB of a given `length`.

    The result has at least:
    - one uppercase letter
    - one lowercase letter
    - one digit
    - one special character

    Raises:
        ValueError -- If `length` is lesser than 8.
    """
    if length < 8:
        raise ValueError("Password length should be at least 8")

    return generate_random_string(
        length,
        string.ascii_uppercase, # в пароле должны быть заглавные буквы
        string.ascii_lowercase, # и строчные
        string.digits, # и цифры
        "!&?", # и спец-символы, добавьте нужных по вкусу
    )

	
#нужно вызвать функцию, где в скобках длина пароля generate_mydb_password()