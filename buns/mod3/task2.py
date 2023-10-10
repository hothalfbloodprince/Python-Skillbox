number = int(input())
forms =', '.join([bin(number)[2:], oct(number)[2:], hex(number)[2:]])
print(forms if number > 0 else 'Неверный ввод')