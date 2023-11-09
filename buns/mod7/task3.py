import time


def memoize(func):
    cache = {}

    def wrapper(*args):
        if args in cache:
            return cache[args]
        result = func(*args)
        cache[args] = result
        return result
    return wrapper


def fibonacci(n):
    if n <= 1:
        return n
    else:
        return fibonacci(n-1) + fibonacci(n-2)


def timer(func):
    def wrapper(*args, **kwargs):
        start_time = time.time()
        result = func(*args, **kwargs)
        end_time = time.time()
        execution_time = end_time - start_time
        print(f"Функция {func.__name__} выполнилась за {execution_time} секунд")
        return result
    return wrapper


@memoize
@timer
def get_fibonacci_memoize(n):
    return fibonacci(n)


@timer
def get_fibonacci(n):
    return fibonacci(n)


print(get_fibonacci_memoize(35))
print(get_fibonacci(35))
