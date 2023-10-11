first_len = input()
k = len(first_len)
field = [list(input()) for _ in range(k - 1)]
field.insert(0, list(first_len))

def check_winner(field):
    # Проверка по строкам
    for row in field:
        if row.count('X') == k:
            return 'X'
        elif row.count('O') == k:
            return 'O'

    # Проверка по столбцам
    for col in range(k):
        column = [field[row][col] for row in range(k)]
        if column.count("X") == k:
            return 'X'
        elif column.count("O") == k:
            return 'O'

    # Проверка по диагоналям
    diag_one = [field[i][i] for i in range(k)]
    if diag_one.count("X") == k:
        return 'X'
    elif diag_one.count("O") == k:
        return 'O'

    diag_two = [field[i][k-1-i] for i in range(k)]
    if diag_two.count("X") == k:
        return 'X'
    elif diag_two.count("O") == k:
        return 'O'

    return 'Ничья'

print(check_winner(field))