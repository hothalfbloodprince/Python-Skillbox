def get_generator():
    for num in range(10, 10 ** 10):
        order = len(str(num))
        sum_of_powers = sum(int(digit) ** order for digit in str(num))
        if num == sum_of_powers:
            yield num

generator = get_generator()
def get_armstrong_numbers():
    return next(generator)

for i in range(8):
    print(get_armstrong_numbers(), end=' ')