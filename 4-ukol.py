# Funkce kontrola telefonního čísla
def check_input(cislo):
    pocet_cisel = len(cislo)

    if pocet_cisel == 9 or pocet_cisel == 13:
        return True
    else:
        return False

# Funkce kontrola textu a výpočet ceny
def check_text(text):
    delka = len(text)
    cena = delka/180
    from math import ceil
    cena_zaokr = ceil(cena)*3
    return cena_zaokr

# Funkce pro kontrolu předvolby
def check_areacode(predvolba):
    predvolba = telefonni_cislo[0:3]
    
    if telefonni_cislo == 13:
        predvolba[0:3] == +420
        return True
    else:
        return False 


telefonni_cislo = input("Zadejte telefonní číslo příjemce:")
predvolba = telefonni_cislo[0:3]

if check_input(telefonni_cislo) == True:
        predvolba = check_areacode(predvolba)
        text = input("Zde zadejte text Vaší zprávy:")
        cena = check_text(text)
        print("Cena zprávy: " + str(cena))
else:
    print ('Chybný formát čísla!')
