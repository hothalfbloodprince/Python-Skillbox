numbers = input()
space_counter = 0
len_first_numb = 0
len_second_numb = 0
middle_numb = 0

for element in numbers:
    if element == ' ':
        space_counter += 1
    if space_counter < 1:
        len_first_numb += 1
    elif space_counter == 1:
        len_second_numb += 1
    else:
        break

first_numb = int(numbers[:len_first_numb])
second_numb = int(numbers[len_first_numb + 1: len_first_numb + len_second_numb])
third_numb = int(numbers[len_first_numb + len_second_numb + 1:])

if (first_numb >= second_numb) and (third_numb <= second_numb) or (first_numb <= second_numb) and (third_numb >= second_numb):
    middle_numb = second_numb
elif (first_numb >= third_numb) and (second_numb <= third_numb) or (first_numb <= third_numb) and (second_numb >= third_numb):
    middle_numb = third_numb
else:
    middle_numb = first_numb

print(middle_numb)