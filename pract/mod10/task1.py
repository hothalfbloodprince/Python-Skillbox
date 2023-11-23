import re
import doctest


def validate_password(password):
    """
    Функция, проверяющая корректность пароля

    Args:
    password (str): Пароль.

    Returns:
    bool: Корректность пароля.

    >>> validate_password("rtG3FG!Tr^e")
    True
    >>> validate_password("aA1!*!1Aa")
    True
    >>> validate_password("oF^a1D@y5e6")
    True
    >>> validate_password("enroi#$rkdeR#$092uWedchf34tguv394h")
    True
    >>> validate_password("пароль")
    False
    >>> validate_password("password")
    False
    >>> validate_password("qwerty")
    False
    >>> validate_password("lOngPa$$$W0Rd")
    False
    >>> validate_password("000abcd")
    False
    >>> validate_password("AbCdfgw")
    False
    >>> validate_password("12345231")
    False
    >>> validate_password("AB3")
    False
    """
    pattern = (
        r'^(?=.*[A-Z].*[A-Z])'
        r'(?=.*\d)'
        r'(?=.*[^A-Za-z0-9])'
        r'(?!.*(.)\1\1)'
        r'[A-Za-z0-9^$%@#&*!?]{6,}$'
    )
    return re.match(pattern, password) is not None


doctest.testmod()
