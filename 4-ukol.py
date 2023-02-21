# Funkce kontrola telefonního čísla
# def check_input(cislo):
#     pocet_cisel = len(cislo)

#     if pocet_cisel == 9 or pocet_cisel == 13:
#         return True
#     else:
#         return False

def check_input(cislo):
    pocet_cisel = len(cislo)
    return pocet_cisel == 9 or check_areacode(cislo) 


# Funkce kontrola textu a výpočet ceny
def check_text(text):
    delka = len(text)
    cena = delka/180
    from math import ceil
    cena_zaokr = ceil(cena)*3
    return cena_zaokr

# Funkce pro kontrolu předvolby
def check_areacode(cislo):
    predvolba = cislo[0:4]
    return len(cislo) == 13 and predvolba ==  '+420'


telefonni_cislo = input("Zadejte telefonní číslo příjemce:")
predvolba = cislo[0:4]

if check_input(telefonni_cislo):
        text = input("Zde zadejte text Vaší zprávy:")
        cena = check_text(text)
        print("Cena zprávy: " + str(cena))
else:
    print ('Chybný formát čísla!')
