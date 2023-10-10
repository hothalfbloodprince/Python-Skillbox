lower_limit, upper_limit = 32, 126 #надеюсь, здесь тоже нужен был ввод(зато нет магических чисел)
chars = [chr(i) for i in range(lower_limit, upper_limit + 1)]
print(''.join(chars))