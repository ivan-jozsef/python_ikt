def Fogl():
    asztalok = []
    terem = int(input("Enter your option: [1. TeremA, 2. TeremB, 3. TeremC]" ))-1
    for elem in foglalasok:
         asztalok.append(elem[terem])
      
    #print(f"asztalok = {asztalok}")
    asztalbeker = int(input("Kérem adja meg az asztal számát 1-8: "))-1
    #print(f"asztalok = {asztalok[asztalbeker]}")
    szekbeker = int(input("Kérem adja meg a szék számát 1-10: " ))-1
    #print(f"szék = {asztalok[asztalbeker][szekbeker]}")
    szekek = list(asztalok[asztalbeker])  #székek nevű uj tömböt hoztunk létre
    
    

    valasz = False
    while valasz == False:
        if szekek[szekbeker] == "1":
            print("Az Ön által választott asztal foglalt, kérem válasszon másik asztalt!")
            asztalbeker = int(input("Kérem adja meg az asztal számát 1-8: "))-1
            szekbeker = int(input("Kérem adja meg a szék számát 1-10: " ))-1
            
        else:
            szekek[szekbeker] = "1"
            foglalasok[asztalbeker][terem] = ''.join(str(e) for e in szekek)
            #print(foglalasok)
            print("Köszönjük az asztalt lefoglaltuk az Ön részére!")
            print(f"eredetiasztal = {asztalok[asztalbeker]}")
            print(f"cseréltasztal = {foglalasok[asztalbeker][terem]}")
            valasz = True 
        


#######################################################################
    
valasz= 0
option = int(input("Enter your option: [1. Monday morning, 2. Monday afternoon, 3. Monday evening,  0. Kilépés] "))

while valasz == 0:
    foglalasok = []
    if option == 1:
        
        with open("Monday_morning.txt", "r", encoding="utf-8") as file:
            elsosor = file.readline()
            tobbisor = file.readlines()
            for sor in tobbisor:
                adatok = sor.strip().split("     ")
                helyek = []
                for szek in adatok:
                    helyek.append(szek.replace(' ',''))
                    continue
                foglalasok.append(helyek)
        
        #print(foglalasok)
        valasz = 1
        Fogl()
           
            
    elif option == 2:
        with open("Monday_afternoon.txt", "r", encoding="utf-8") as file:
            elsosor = file.readline()
            tobbisor = file.readlines()
            for sor in tobbisor:
                adatok = sor.strip().split("     ")
                helyek = []
                for szek in adatok:
                    helyek.append(szek.replace(' ',''))
                    continue
                foglalasok.append(helyek)
        
        print(foglalasok)
        valasz = 1
        Fogl()
            
    elif option == 3:
        with open("Monday_evening.txt", "r", encoding="utf-8") as file:
            elsosor = file.readline()
            tobbisor = file.readlines()
            for sor in tobbisor:
                adatok = sor.strip().split("     ")
                helyek = []
                for szek in adatok:
                    helyek.append(szek.replace(' ',''))
                    continue
                foglalasok.append(helyek)
        
        print(foglalasok)
        valasz = 1
        Fogl()
            
    else:
        print("Invalid Option")
        option = int(input("Enter your option: [1. Monday morning, 2. Monday afternoon, 3. Monday evening,  0. Kilépés] "))

