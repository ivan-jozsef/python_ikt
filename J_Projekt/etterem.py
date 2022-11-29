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
########################################################################################################################
#Egy adott napszakról készült fájlkiírás listába 'rendezése'
foglalasok = []

# with open('Monday_morning.txt', 'r', encoding='utf-8') as forras:
#     elso_sor = forras.readline()
#     tobbi_sor = forras.readlines()
#     # print(tobbi_sor)
#     for sor in tobbi_sor:
#         adatok = sor.strip().split(' ')
#         # print(adatok)
#         foglalasok.append(adatok)
#     # print(adatok)#
#     # print(foglalasok)#
#     adatok2 = []
#     for terem in foglalasok:
#         for hely in terem:
#             if hely.strip():
#                 adatok2.append(hely)

# print(foglalasok)
# print(adatok2)
# print(len(adatok2))
#az alábbi folyamat eltávolítja a ''-et az adatok közül. Jelen esetben a Monday morning termei soronként
for i in range(4):
    for sorok in foglalasok:
        for helyek in sorok:
            if helyek == '':
                sorok.remove('')

# print(foglalasok)
# print("3 terem első sorai:", len(foglalasok[0]))
# print("3 terem második sorai:", len(foglalasok[1]))
# print("3 terem harmadik sorai:", len(foglalasok[2]))
# print("3 terem negyedik sorai:", len(foglalasok[3]))
# print("3 terem ötödik sorai:", len(foglalasok[4]))
# print("3 terem hatodik sorai:", len(foglalasok[5]))
# print("3 terem hetedik sorai:", len(foglalasok[6]))
# print("3 terem nyolcadik sorai:", len(foglalasok[7]))

#B verzió
foglalasok = []
with open('Monday_morning.txt', 'r', encoding='utf-8') as forras:
    elso_sor = forras.readline()
    tobbi_sor = forras.readlines()
#     print(tobbi_sor, '\n')#
    for sor in tobbi_sor:
#         print(sor)
        adatok = sor.strip().split("     ")
#         print("ADATOK: ", adatok)
        sorok = []
        for padok in adatok:
#             print("PADOK: ", padok)
            sorok.append(padok.replace(' ',''))
#             print("SOROK: ", sorok)
            continue
        foglalasok.append(sorok)
#         print("TERMEK: ", foglalasok)

# print("Foglalasok", foglalasok)
########################################################################################################################

#Menürendszer az adott napszak bevételeinek lekérdezéséhez
option = int(input("Enter your option: [1. Monday morning, 2. Monday afternoon, 3. Monday evening, 4. All income on Monday, 0. Kilépés] "))

while option != 0:
    if option == 1:
        with open("Monday_morning.txt", "r", encoding="utf-8") as file:
            tartalom = file.read()
            print(tartalom)
            osszbevetel = 0
            for ar in tartalom:
                if ar == '1':
                    osszbevetel += 1
            print(f"Az étterem Hétfő reggeli bevétele {osszbevetel * 4000} HUF")
    elif option == 2:
        with open("Monday_afternoon.txt", "r", encoding="utf-8") as file:
            tartalom = file.read()
            print(tartalom)
            osszbevetel = 0
            for ar in tartalom:
                if ar == '1':
                    osszbevetel += 1
            print(f"Az étterem Hétfő délutáni bevétele {osszbevetel * 4000} HUF")
    elif option == 3:
        with open("Monday_evening.txt", "r", encoding="utf-8") as file:
            tartalom = file.read()
            print(tartalom)
            osszbevetel = 0
            for ar in tartalom:
                if ar == '1':
                    osszbevetel += 1
            print(f"Az étterem Hétfő esti bevétele {osszbevetel * 4000} HUF")
    elif option == 4:
        with open("Monday_morning.txt", "r", encoding="utf-8") as file:
            tartalom = file.read()
            print(tartalom)
        with open("Monday_afternoon.txt", "r", encoding="utf-8") as file2:
            tartalom2 = file2.read()
            print(tartalom)
        with open("Monday_evening.txt", "r", encoding="utf-8") as file3:
            tartalom3 = file3.read()
            print(tartalom)
            osszbevetel = 0
            for ar in tartalom:
                if ar == '1':
                    osszbevetel += 1
            for ar in tartalom2:
                if ar == '1':
                    osszbevetel += 1
            for ar in tartalom3:
                if ar == '1':
                    osszbevetel += 1
            print(f"Az étterem Hétfői összbevétele {osszbevetel * 4000} HUF")
    else:
        print("Invalid Option")
    option = int(input("Enter your option: [1. Monday morning, 2. Monday afternoon, 3. Monday evening, 4. All income on Monday, 0. Kilépés] "))
########################################################################################################################

#Egy adott napszak bevételeinek kiszámítása
osszbevetel = 0

for ar in foglalasok:
    if ar == '1':
        osszbevetel += 1
print(f"Az étterem aznapi bevétele {osszbevetel*4000} HUF")

########################################################################################################################