# chap 6-1
for k in [3, 2, 1, 0]:
    print(k)

# chap 6-2

guess_me = 7
number = 1
while True:
    if number < guess_me:
        print('too low')
    elif    number == guess_me:
        print('found it')
        break
    elif    number > guess_me:
        print('oops')
        break
    number += 1







