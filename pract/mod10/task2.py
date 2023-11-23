import re
import doctest


def validate_color(color):
    """
    Функция, проверяющая корректность web цвета

    Args:
    color (str): Цвет.

    Returns:
    bool: Корректность цвета.

    >>> validate_color("#21f48D")
    True
    >>> validate_color("#888")
    True
    >>> validate_color("rgb(255, 255,255)")
    True
    >>> validate_color("rgb(10%, 20%, 0%)")
    True
    >>> validate_color("hsl(200,100%,50%)")
    True
    >>> validate_color("hsl(0, 0%, 0%)")
    True
    >>> validate_color("#2345")
    False
    >>> validate_color("ffffff")
    False
    >>> validate_color("rgb(257, 50, 10)")
    False
    >>> validate_color("hsl(20, 10, 0.5)")
    False
    >>> validate_color("hsl(34%, 20%, 50%)")
    False
    >>> validate_color("000")
    False
    >>> validate_color("abc")
    False
    >>> validate_color("12345")
    False
    """
    pattern = (
        r'^(#(?:[0-9a-fA-F]{3}){1,2}|'
        r'rgb\((\d{1,2}%?|1\d{1,2}|2[0-4]\d|25[0-5]),\s*'
        r'(\d{1,2}%?|1\d{1,2}|2[0-4]\d|25[0-5]),\s*'
        r'(\d{1,2}%?|1\d{1,2}|2[0-4]\d|25[0-5])\)|'
        r'hsl\(\d{1,3},\s*\d{1,3}%?,\s*\d{1,3}%?\))$'
    )

    return re.match(pattern, color) is not None


doctest.testmod()
