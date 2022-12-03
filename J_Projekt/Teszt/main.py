import random
import os.path

#Előzetes foglalások a hétre random generátorral, meghívással###########################################################


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
#Főmenü#################################################################################################################


def menu():
   print("1. Foglalás")
   print("2. Bevétel ellenőrzés")
   print("3. Kilépés")


########################################################################################################################
#####################################NAPI FOGLALÁS KEZELÉSE#####################################################ANDREA##


def Fogl():
    asztalok = []
    terem = int(input("Enter your option: [1. TeremA, 2. TeremB, 3. TeremC]")) - 1
    for elem in foglalasok:
        asztalok.append(elem[terem])

    # print(f"asztalok = {asztalok}")
    asztalbeker = int(input("Kérem adja meg az asztal számát 1-8: ")) - 1
    # print(f"asztalok = {asztalok[asztalbeker]}")
    szekbeker = int(input("Kérem adja meg a szék számát 1-10: ")) - 1
    # print(f"szék = {asztalok[asztalbeker][szekbeker]}")
    szekek = list(asztalok[asztalbeker])  # székek nevű uj tömböt hoztunk létre

    valasz = False
    while valasz == False:
        if szekek[szekbeker] == "1":
            print("Az Ön által választott asztal foglalt, kérem válasszon másik asztalt!")
            asztalbeker = int(input("Kérem adja meg az asztal számát 1-8: ")) - 1
            szekbeker = int(input("Kérem adja meg a szék számát 1-10: ")) - 1

        else:
            szekek[szekbeker] = "1"
            foglalasok[asztalbeker][terem] = ''.join(str(e) for e in szekek)
            # print(foglalasok)
            print("Köszönjük az asztalt lefoglaltuk az Ön részére!")
            print(f"eredetiasztal = {asztalok[asztalbeker]}")
            print(f"cseréltasztal = {foglalasok[asztalbeker][terem]}")
            valasz = True


########################################################################################################################
#########################################TEREMFÁJLOK ELŐKÉSZÍTÉSE#######################################################


foglalasok = []
def listakeszites():
    elso_sor = forras.readline()
    tobbi_sor = forras.readlines()
#     print(tobbi_sor, '\n')#
    for sor in tobbi_sor:
#         print(sor)
        adatok = sor.strip().split("     ")
        # print("ADATOK: ", adatok)
        sorok = []
        for padok in adatok:
            # print("PADOK: ", padok)
            sorok.append(padok.replace(' ',''))
            # print("SOROK: ", sorok)
            continue
        foglalasok.append(sorok)
print(foglalasok)
########################################################################################################################
########################################## LISTÁK VISSZAALAKÍTÁSA ######################################################


def lista_visszaalakitasa():
        # with open('Morning.txt', 'w+', encoding="utf-8") as cel:
        #     print("     ", "TeremA", "                ", "TeremB", "                ", "TeremC", file=cel)
        #     for sorok in foglalasok:
        #         for termek in sorok:
        #             print(sorok, file=cel)
    with open('Morning.txt', 'w', encoding="utf-8") as cel:
        print("     ", "TeremA", "                ", "TeremB", "                ", "TeremC", file=cel)
        for sorok in foglalasok:
            for index, padok in enumerate(sorok):
                for szekek in padok:
                    print(szekek, end=' ', file=cel)
                if index <= 1:
                    print(end='    ', file=cel)
                elif index == 2:
                    print(end='\n', file=cel)

########################################################################################################################
#Létrehozza a hét napjainak megfelelő mappákat (egyszer)################################################################


if not os.path.exists('Monday'):
    os.mkdir('Monday')
if not os.path.exists('Tuesday'):
    os.mkdir('Tuesday')
if not os.path.exists('Wednesday'):
    os.mkdir('Wednesday')
if not os.path.exists('Thursday'):
    os.mkdir('Thursday')
if not os.path.exists('Friday'):
    os.mkdir('Friday')
if not os.path.exists('Saturday'):
    os.mkdir('Saturday')
if not os.path.exists('Sunday'):
    os.mkdir('Sunday')


########################################################################################################################
#A hétfői nap asztalfoglalásai napszakonként elválasztva, fájlba generálás##############################################


for nap in range(21):
    if not os.path.exists('Monday/Morning.txt'):
        with open('Monday/Morning.txt', 'x', encoding='utf-8') as celfajl:
            prebooking()
    elif not os.path.exists('Monday/Afternoon.txt'):
        with open('Monday/Afternoon.txt', 'x', encoding='utf-8') as celfajl:
            prebooking()
    elif not os.path.exists('Monday/Evening.txt'):
        with open('Monday/Evening.txt', 'x', encoding='utf-8') as celfajl:
            prebooking()
    elif not os.path.exists('Tuesday/Morning.txt'):
        with open('Tuesday/Morning.txt', 'x', encoding='utf-8') as celfajl:
            prebooking()
    elif not os.path.exists('Tuesday/Afternoon.txt'):
        with open('Tuesday/Afternoon.txt', 'x', encoding='utf-8') as celfajl:
            prebooking()
    elif not os.path.exists('Tuesday/Evening.txt'):
        with open('Tuesday/Evening.txt', 'x', encoding='utf-8') as celfajl:
            prebooking()
    elif not os.path.exists('Wednesday/Morning.txt'):
        with open('Wednesday/Morning.txt', 'x', encoding='utf-8') as celfajl:
            prebooking()
    elif not os.path.exists('Wednesday/Afternoon.txt'):
        with open('Wednesday/Afternoon.txt', 'x', encoding='utf-8') as celfajl:
            prebooking()
    elif not os.path.exists('Wednesday/Evening.txt'):
        with open('Wednesday/Evening.txt', 'x', encoding='utf-8') as celfajl:
            prebooking()
    elif not os.path.exists('Thursday/Morning.txt'):
        with open('Thursday/Morning.txt', 'x', encoding='utf-8') as celfajl:
            prebooking()
    elif not os.path.exists('Thursday/Afternoon.txt'):
        with open('Thursday/Afternoon.txt', 'x', encoding='utf-8') as celfajl:
            prebooking()
    elif not os.path.exists('Thursday/Evening.txt'):
        with open('Thursday/Evening.txt', 'x', encoding='utf-8') as celfajl:
            prebooking()
    elif not os.path.exists('Friday/Morning.txt'):
        with open('Friday/Morning.txt', 'x', encoding='utf-8') as celfajl:
            prebooking()
    elif not os.path.exists('Friday/Afternoon.txt'):
        with open('Friday/Afternoon.txt', 'x', encoding='utf-8') as celfajl:
            prebooking()
    elif not os.path.exists('Friday/Evening.txt'):
        with open('Friday/Evening.txt', 'x', encoding='utf-8') as celfajl:
            prebooking()
    elif not os.path.exists('Saturday/Morning.txt'):
        with open('Saturday/Morning.txt', 'x', encoding='utf-8') as celfajl:
            prebooking()
    elif not os.path.exists('Saturday/Afternoon.txt'):
        with open('Saturday/Afternoon.txt', 'x', encoding='utf-8') as celfajl:
            prebooking()
    elif not os.path.exists('Saturday/Evening.txt'):
        with open('Saturday/Evening.txt', 'x', encoding='utf-8') as celfajl:
            prebooking()
    elif not os.path.exists('Sunday/Morning.txt'):
        with open('Sunday/Morning.txt', 'x', encoding='utf-8') as celfajl:
            prebooking()
    elif not os.path.exists('Sunday/Afternoon.txt'):
        with open('Sunday/Afternoon.txt', 'x', encoding='utf-8') as celfajl:
            prebooking()
    elif not os.path.exists('Sunday/Evening.txt'):
        with open('Sunday/Evening.txt', 'x', encoding='utf-8') as celfajl:
            prebooking()
    else:
        pass


########################################################################################################################
####################################FŐMENÜ BETÖLTÉSE####################################################################


menu()

valasztas = int(input("Válasszon  a menüből!"))

while valasztas != 3:
    if valasztas == 1:
        valasz = 0
        nap = int(input("Enter your option: [1. Monday, 2. Tuesday, 3. Wednesday, 4. Thursday, 5. Friday, 6. Saturday, 7. Sunday, 0. Kilépés] "))
        option = int(input("Enter your option: [1. morning, 2. afternoon, 3. evening, 0. Kilépés] "))

        while valasz == 0:
            foglalasok = []
            with open("Monday/Morning.txt", "r", encoding="utf-8") as file:
                tartalom = file.read()
                print(tartalom)
            if option == 1 and nap == 1:
                with open("Monday/Morning.txt", "r", encoding="utf-8") as file:
                    print("Válassza ki a termet, majd a sort, végül pedig a széket, amit foglalni szeretne!")
                    elsosor = file.readline()
                    tobbisor = file.readlines()
                    # print(tartalom)
                    for sor in tobbisor:
                        adatok = sor.strip().split("     ")
                        helyek = []
                        for szek in adatok:
                            helyek.append(szek.replace(' ', ''))
                            continue
                        foglalasok.append(helyek)
                # print(foglalasok)
                valasz = 1
                Fogl()
                lista_visszaalakitasa()



            elif option == 2 and nap == 1:
                with open("Monday/Afternoon.txt", "r", encoding="utf-8") as file:
                    elsosor = file.readline()
                    tobbisor = file.readlines()
                    for sor in tobbisor:
                        adatok = sor.strip().split("     ")
                        helyek = []
                        for szek in adatok:
                            helyek.append(szek.replace(' ', ''))
                            continue
                        foglalasok.append(helyek)

                # print(foglalasok)
                valasz = 1
                Fogl()

            elif option == 3 and nap == 1:
                with open("Monday/Evening.txt", "r", encoding="utf-8") as file:
                    elsosor = file.readline()
                    tobbisor = file.readlines()
                    for sor in tobbisor:
                        adatok = sor.strip().split("     ")
                        helyek = []
                        for szek in adatok:
                            helyek.append(szek.replace(' ', ''))
                            continue
                        foglalasok.append(helyek)

                print(foglalasok)
                valasz = 1
                Fogl()

            else:
                print("Invalid Option")
                option = int(input("Enter your option: [1. Monday morning, 2. Monday afternoon, 3. Monday evening,  0. Kilépés] "))

    elif valasztas == 2:
        pass
    else:
        print("Nem létező menüt próbál megnyitni, próbálja újból!")
        menu()
        print(int(input("Válasszon  a menüből!")))

print("Kilépett a programból!")


########################################################################################################################
##########################################TEREMFÁJLOK ELŐKÉSZÍTÉSE######################################################


with open('Monday/Morning.txt', 'r', encoding='utf-8') as forras:
    listakeszites()
print(foglalasok)

########################################################################################################################



