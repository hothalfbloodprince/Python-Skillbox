phone_number = input()
new_number = phone_number.replace(' (', '').replace(') ', '').replace('-', '')
print(new_number)