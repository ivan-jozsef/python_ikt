import os

def wed_e():
    termek = list()
    asztalok = list()

    count = 0
    with open("Wednesday\Afternoon.txt",'r') as fp:
        Lines = fp.readlines()
        for line in Lines:
            count += 1
            adat = line.strip().replace(" ", "")
            if adat != "      " or adat != " ":
                asztalok.append(adat)
            else:
                termek.append(asztalok)
                asztalok=[]
    # print(asztalok)

    harom_asztal = []
    for szek in asztalok:
        sub = szek.split(', ')
        harom_asztal.append(sub)


    # print(harom_asztal)
    # print("######################################################")
    # print(harom_asztal[1])
    # print("######################################################")

    #elsosor
    szovegalakit1 = str(harom_asztal[1])
    szamlalo1 =0
    for egy in szovegalakit1:
        if egy == '1':
            szamlalo1 += 1
    #print(f'A sztringben {szamlalo1} db 1 -es van')

    #masodiksor
    szovegalakit2 = str(harom_asztal[2])
    szamlalo2 =0
    for egy in szovegalakit2:
        if egy == '1':
            szamlalo2 += 1
    #print(f'A sztringben {szamlalo2} db 1 -es van')

    #harmadiksor
    szovegalakit3 = str(harom_asztal[3])
    szamlalo3 =0
    for egy in szovegalakit3:
        if egy == '1':
            szamlalo3 += 1
    #print(f'A sztringben {szamlalo3} db 1 -es van')

    #negyediksor
    szovegalakit4 = str(harom_asztal[4])
    szamlalo4 =0
    for egy in szovegalakit4:
        if egy == '1':
            szamlalo4 += 1
    #print(f'A sztringben {szamlalo4} db 1 -es van')

    #otodiksor
    szovegalakit5 = str(harom_asztal[5])
    szamlalo5 =0
    for egy in szovegalakit5:
        if egy == '1':
            szamlalo5 += 1
    #print(f'A sztringben {szamlalo5} db 1 -es van')

    #hatodiksor
    szovegalakit6 = str(harom_asztal[6])
    szamlalo6 =0
    for egy in szovegalakit6:
        if egy == '1':
            szamlalo6 += 1
    #print(f'A sztringben {szamlalo6} db 1 -es van')

    #hetediksor
    szovegalakit7 = str(harom_asztal[7])
    szamlalo7 =0
    for egy in szovegalakit7:
        if egy == '1':
            szamlalo7 += 1
    #print(f'A sztringben {szamlalo7} db 1 -es van')

    #nyolcadiksor
    szovegalakit8 = str(harom_asztal[8])
    szamlalo8 =0
    for egy in szovegalakit8:
        if egy == '1':
            szamlalo8 += 1
    #print(f'A sztringben {szamlalo8} db 1 -es van')
    global wed_eo
    wed_eo = ((szamlalo1 + szamlalo2 + szamlalo3 + szamlalo4 + szamlalo5 + szamlalo6 + szamlalo7 + szamlalo8) * 4000)
    print("*******************************************************************************")
    print(f'Szerda este összesen {(szamlalo1 + szamlalo2 + szamlalo3 +szamlalo4+ szamlalo5 + szamlalo6 + szamlalo7 + szamlalo8) * 4000} Ft volt a bevétel.')
    print("*******************************************************************************")

    #print(harom_asztal)
    #print(szovegalakit1)
    #print(len(szovegalakit1))
    #print(len(szovegalakit1[0:12]))
    #print(szovegalakit1[2:12])
    #print(szovegalakit1[12:22])
    #print(len(szovegalakit1[12:22]))
    #print(szovegalakit1[12:22])
    #print(len(szovegalakit1[12:22]))
    #print("###########################")
    #print(szovegalakit1[22:32])
    #print(len(szovegalakit1[22:32]))

    aterem_elso = szovegalakit1[2:12].count('1') * 4000
    aterem_masodik = szovegalakit2[2:12].count('1') * 4000
    aterem_harmadik = szovegalakit3[2:12].count('1') * 4000
    aterem_negyedik = szovegalakit4[2:12].count('1') * 4000
    aterem_otodik = szovegalakit5[2:12].count('1') * 4000
    aterem_hatodik = szovegalakit6[2:12].count('1') * 4000
    aterem_hetedik = szovegalakit7[2:12].count('1') * 4000
    aterem_nyolcadik = szovegalakit8[2:12].count('1') * 4000
    print(f'TeremA 1. asztal bevétele: {aterem_elso} Ft.')
    print(f'TeremA 2. asztal bevétele: {aterem_masodik} Ft.')
    print(f'TeremA 3. asztal bevétele: {aterem_harmadik} Ft.')
    print(f'TeremA 4. asztal bevétele: {aterem_negyedik} Ft.')
    print(f'TeremA 5. asztal bevétele: {aterem_otodik} Ft.')
    print(f'TeremA 6. asztal bevétele: {aterem_hatodik} Ft.')
    print(f'TeremA 7. asztal bevétele: {aterem_hetedik} Ft.')
    print(f'TeremA 8. asztal bevétele: {aterem_nyolcadik} Ft.')
    # TeremA összbevétel:
    ateremossz = aterem_elso + aterem_masodik + aterem_harmadik + aterem_negyedik + aterem_otodik + aterem_hatodik + aterem_hetedik + aterem_nyolcadik
    print(f'A TeremA összbevétele: {ateremossz} Ft ')

    bterem_elso = szovegalakit1[12:22].count('1') * 4000
    bterem_masodik = szovegalakit2[12:22].count('1') * 4000
    bterem_harmadik = szovegalakit3[12:22].count('1') * 4000
    bterem_negyedik = szovegalakit4[12:22].count('1') * 4000
    bterem_otodik = szovegalakit5[12:22].count('1') * 4000
    bterem_hatodik = szovegalakit6[12:22].count('1') * 4000
    bterem_hetedik = szovegalakit7[12:22].count('1') * 4000
    bterem_nyolcadik = szovegalakit8[12:22].count('1') * 4000
    print(f'TeremB 1. asztal bevétele: {bterem_elso} Ft.')
    print(f'TeremB 2. asztal bevétele: {bterem_masodik} Ft.')
    print(f'TeremB 3. asztal bevétele: {bterem_harmadik} Ft.')
    print(f'TeremB 4. asztal bevétele: {bterem_negyedik} Ft.')
    print(f'TeremB 5. asztal bevétele: {bterem_otodik} Ft.')
    print(f'TeremB 6. asztal bevétele: {bterem_hatodik} Ft.')
    print(f'TeremB 7. asztal bevétele: {bterem_hetedik} Ft.')
    print(f'TeremB 8. asztal bevétele: {bterem_nyolcadik} Ft.')
    # TeremB összbevétel:
    bteremossz = bterem_elso + bterem_masodik + bterem_harmadik + bterem_negyedik + bterem_otodik + bterem_hatodik + bterem_hetedik + bterem_nyolcadik
    print(f'A TeremB összbevétele: {bteremossz} Ft ')


    cterem_elso = szovegalakit1[22:32].count('1') * 4000
    cterem_masodik = szovegalakit2[22:32].count('1') * 4000
    cterem_harmadik = szovegalakit3[22:32].count('1') * 4000
    cterem_negyedik = szovegalakit4[22:32].count('1') * 4000
    cterem_otodik = szovegalakit5[22:32].count('1') * 4000
    cterem_hatodik = szovegalakit6[22:32].count('1') * 4000
    cterem_hetedik = szovegalakit7[22:32].count('1') * 4000
    cterem_nyolcadik = szovegalakit8[22:32].count('1') * 4000
    print(f'TeremC 1. asztal bevétele: {cterem_elso} Ft.')
    print(f'TeremC 2. asztal bevétele: {cterem_masodik} Ft.')
    print(f'TeremC 3. asztal bevétele: {cterem_harmadik} Ft.')
    print(f'TeremC 4. asztal bevétele: {cterem_negyedik} Ft.')
    print(f'TeremC 5. asztal bevétele: {cterem_otodik} Ft.')
    print(f'TeremC 6. asztal bevétele: {cterem_hatodik} Ft.')
    print(f'TeremC 7. asztal bevétele: {cterem_hetedik} Ft.')
    print(f'TeremC 8. asztal bevétele: {cterem_nyolcadik} Ft.')
    # TeremC összbevétel:
    cteremossz = cterem_elso + cterem_masodik + cterem_harmadik + cterem_negyedik + cterem_otodik + cterem_hatodik + cterem_hetedik + cterem_nyolcadik
    print(f'A TeremC összbevétele: {cteremossz} Ft ')
    print(f'Kontroll összeg: {ateremossz + bteremossz + cteremossz} Ft')

wed_e()

we = wed_eo