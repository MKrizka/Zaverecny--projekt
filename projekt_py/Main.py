from pojistenec import Pojistenec
from funkce_system import Funkce_system


volba = 0
system = Funkce_system()
seznam_pojistencu = []
pojistenec = Pojistenec
pokracovat = "y"

    
    
while pokracovat == "y":

    system.moznosti()



    volba = int(input("Zadej vaši volbu: "))
    if volba == 1:
        print("Zvolili jste si volbu číslo 1 _ přidání pojištěnce")
        jmeno = input("Zadejte jméno pojištěnce: ")
        prijmeni = input("Zadejte příjmení pojištěnce: ")
        vek = input("Zadejte věk pojištěnce: ")
        telefon = input("Zadejtejte telefonní číslo pojištěnce: ")
        novy_pojistenec = Pojistenec(jmeno,prijmeni,vek,telefon)
        print(novy_pojistenec)
        seznam_pojistencu.append(novy_pojistenec)

    elif volba == 2:
        print("Zvolili jste si volbu číslo 2 _ vypsání všech pojištěnců")
        print("Jméno ; Příjmení ; Věk ; Telefonní číslo\n")
        for pojistenec in seznam_pojistencu:
            print(pojistenec)

    elif volba == 3:
        print("Zvolili jste si volbu číslo 3 _ vyhledání pojištěnce")
        jmeno_input = input("Hledáné jméno: ")
        prijmeni_input = input("hledané prijmei: ")
            
        for pojistenec in seznam_pojistencu:
            if(jmeno_input == pojistenec.jmeno) and(prijmeni_input == pojistenec.prijmeni):
                print(f"Hledný pojištěnec je zde: {pojistenec}")
            else: print("Pojištěnec není v databázi")

    elif volba == 4:
        print("Zvolili jste si volbu číslo 4 _ ukončení programu")
        print("Děkujeme za využití")
        break
    
    else: print("Zvolili jste neplatnou volbu")

        
    pokracovat = input("\nPrejete si pokračovat? y / n: ")
    if (pokracovat != "y"):
        pokracovat = "False"
        
           
            
        
        
        
        









