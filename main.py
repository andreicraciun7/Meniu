lista_prezenta = ["Ioan", "Ion", "Ionut", "Iosif", "Iacob"]
print("Persoanele prezente sunt:")
print(lista_prezenta)
sir = []
while True:
    print("""
        Pentru a modifica lista, alege una dintre optiunile de mai jos:
        1. Adaugă o persoană
        2. Șterge o persoană
        3. Arată ultimele 3 persoane introduse
        4. Arată persoanele între pozițiile 2 și 4
        5. Arată lista de prezență
       """)


    optiune = input("Selectează o opțiune:")

    if optiune == "1":
        adauga_la_lista = input("Adaugă o persoană: ")
        lista_prezenta.append(adauga_la_lista)

    elif optiune == "2":
        sterge_din_lista = input("Șterge o persoană: ")
        if sterge_din_lista in lista_prezenta:
            lista_prezenta.remove(sterge_din_lista)
        else:
            print("\n Numele introdus nu se află în listă \n")

    elif optiune == "3":
        lista_ultimii = []
        if len(lista_prezenta) >= 3:
            ultimii = lista_prezenta.copy()
            while len(lista_ultimii) <3:
                lista_ultimii.append(ultimii.pop())
            print(lista_ultimii)
        else:
            print("\n Lista conține mai puțin de 3 persoane \n")

    elif optiune == "4":
        sir = lista_prezenta.copy()
        arata_de_la = int(input("\n    Arată lista de la persoana cu numărul: "))
        arata_pana_la = int(input("\n    ... până la persoana cu numărul: "))
        afiseaza_sir_persoane = []
        while arata_de_la -1 <= arata_pana_la -1:
            afiseaza_sir_persoane.append(sir[arata_de_la-1])
            arata_de_la += 1
        print(afiseaza_sir_persoane)


    elif optiune == "5":
        print(lista_prezenta)

    else:
        print("\n Opțiunea introdusă nu este validă \n")
        continue
