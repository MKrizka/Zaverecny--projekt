seznam_pojistencu = []
class Funkce_pojistenci:



    def __init__(self,pojistenec):
        self.pojistenec = pojistenec

    def vytvořeni_pojistence(self):
        print()

    jmeno = input("Jméno: ")
    prijmeni = input("Příjmení: ")
    vek = input("Věk: ")
    telefonní_cislo = input("Telefon: ")

    pojistenec = Pojistenec (jmeno,prijmeni,vek,telefonní_cislo)
    seznam_pojistencu.append(pojistenec)



    def vypsani_pojistenych(self):
        print()
        print("Jméno ; Příjmení ; Věk ; Telefon\n ")
        for pojistenec in seznam_pojistencu:
            print()

    def vyhledani_pojisteneho(self):
        print()

    zadani_jmena = input("Zadej hledané jméno: ")
    zadani_prijmeni = input("Zadej hledané příjmení: ")
    kontrola_seznamu = [pojistenec for pojistenec in seznam_pojistencu if pojistenec.jmeno == zadani_jmena and pojistenec.prijmeni == zadani_prijmeni]
    print()
    print("Jméno ; Příjmení ; Věk ; Telefon\n ")
    for pojistenec in kontrola_seznamu:
        print(pojistenec)




        