side_name = input()
domain = ''

for char in (side_name[::-1]):
    if char != '.':
        domain = char + domain
    else:
        print(domain)
        domain = ''

print(domain)
