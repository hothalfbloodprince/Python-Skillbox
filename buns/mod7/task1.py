def validate_args(func):
    def wrapper(*args):
        if len(args) < 1:
            return "Not enough arguments"
        elif len(args) > 1:
            return "Too many arguments"
        elif not isinstance(args[0], int):
            return "Wrong types"
        elif args[0] < 0:
            return "Negative argument"
        else:
            return func(*args)
    return wrapper

@validate_args
def cur_func(x):
    return x

print(cur_func(2))
print(cur_func())
print(cur_func(5, 7))
print(cur_func("abc"))
print(cur_func(0.15))
print(cur_func(-5))