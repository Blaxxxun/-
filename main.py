import random


def start():
    a = random.randint(1, 6)
    b = random.randint(1, 6)
    if a < b and a != b:
        print('Вы проиграли!')
        print("Ваше число " + str(a))
        print("Число противника " + str(b))
    elif a > b and a != b:
        print('Вы выйграли!')
        print("Ваше число " + str(a))
        print("Число противника " + str(b))
    else:
        print('Ничья!')
        print("Ваше число " + str(a))
        print("Число противника " + str(b))


start()
while True:
    flag = input('Ещё раз? [y/n]: ')

    if flag == 'y':
        print("\n")
        start()
    else:
        break
