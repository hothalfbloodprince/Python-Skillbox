word = input().lower()

letter_count = {}
for letter in word:
    if letter in letter_count:
        letter_count[letter] += 1
    else:
        letter_count[letter] = 1

odd_letter = ''
for letter, count in letter_count.items():
    if count % 2 != 0:
        odd_letter = letter
        break

odd_count = 0
for count in letter_count.values():
    if count % 2 != 0:
        odd_count += 1
        if odd_count > 1:
            break

if odd_count > 1:
    print('Нельзя составить палиндром')
else:
    palindrome = ''
    for letter, count in letter_count.items():
        palindrome += letter * (count // 2)
    palindrome += odd_letter + palindrome[::-1]
    print('Можно составить палиндром:', palindrome)