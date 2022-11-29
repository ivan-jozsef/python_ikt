import random
import os.path

#Előzetes foglalások a hétre random generátorral, meghívással
def prebooking():
    print("     ", "TeremA", "                ", "TeremB", "                ", "TeremC", file=celfajl)
    for i in range(8):
        terem = 1
        while terem <= 3:
            oszlop = 1
            while oszlop <= 10:
                book = random.randint(0, 1)
                print(book, end=' ', file=celfajl)
                oszlop += 1
            print('', end='    ', file=celfajl)
            terem = terem + 1
        print('', file=celfajl)
########################################################################################################################

#A hétfői nap asztalfoglalásai napszakonként elválasztva, fájlba generálás
for nap in range(3):
    if not os.path.exists('Monday_morning.txt'):
        with open('Monday_morning.txt', 'x', encoding='utf-8') as celfajl:
            prebooking()
    elif not os.path.exists('Monday_afternoon.txt'):
        with open('Monday_afternoon.txt', 'x', encoding='utf-8') as celfajl:
            prebooking()
    elif not os.path.exists('Monday_evening.txt'):
        if os.path.exists('Monday_evening.txt'):
            pass
        else:
            with open('Monday_evening.txt', 'x', encoding='utf-8') as celfajl:
                prebooking()
    else:
        print()