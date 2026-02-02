# Напишите генератор generate_random_name(), используя модуль random,
# который генерирует два слова из латинских букв от 1 до 15 символов, разделенных пробелами
# Например при исполнении следующего кода:
# gen = generate_random_name()
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))
#
# Выводится:
# tahxmckzexgdyt ocapwy
# dxqebbukr jg
# aym jpvezfqexlv
# iuy qnikkgxvxfxtxv

import random

# Здесь пишем код
def generate_random_name(num):
    count= 1
    while count <= num:
        str = ""
        for i in range(0, 2):
            n1 = random.randint(1, 15)
            for k in range(0, n1):
                str += random.choice(list("qwertyuiopasdfghjklzxcvbnm"))
            str += " "

        yield str[:len(str)-1]
        count += 1

for gen in generate_random_name(3):
    print(gen)

# gen = generate_random_name(3)
#
# print(next(gen))
# print(next(gen))
# print(next(gen))
# print(next(gen))

