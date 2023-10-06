vowel_li = 'aeiouAEIOU'

while True:
    sent = input()
    if sent == '#':
        break

    result = 0
    for i in sent:
        if i in vowel_li:
            result += 1
    print(result)


