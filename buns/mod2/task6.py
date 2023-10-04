website_name = input()
domain = ''
while len(website_name) > 0:
    char = website_name[0]
    if char != '.':
        domain += char
        website_name = website_name[1::]
    else:
        print(domain)
        website_name = website_name[1::]
        domain = ''
print(domain)
