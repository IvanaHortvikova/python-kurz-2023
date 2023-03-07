# Definice třídy
class Auto:
    def __init__(self, registracni_znacka, typ_vozidla, najete_km, dostuptnost): #metoda
        self.registracni_znacka = registracni_znacka #atributy
        self.typ_vozidla = typ_vozidla
        self.najete_km = najete_km
        self.dostupnost = True
    def pujc_auto(self): #metoda (=funkce)
        if self.dostupnost == True:
            self.dostupnost = False
            return "Potvrzuji zapůjčení vozidla"
        else:
            return "Vozidlo není k dispozici"
        
        
    def get_info(self):
        vysledek = "Registrační značka: " + self.registracni_znacka + "\n"
        vysledek += "Typ vozidla: " + self.typ_vozidla
        return vysledek

#Objekty:
auto1 = Auto("4A2 3020", "Peugeot 403 Cabrio", "47534", "Dostupné")
# print(auto1.pujc_auto())
# print(auto1.pujc_auto())
# print(auto1.get_info())

auto2 = Auto("1P3 4747", "Škoda Octavia", "41253", "Dostupné" )

znacka_auta = input("Vyberte si značku auta, Peugeot nebo Škoda:")
if znacka_auta == "Peugeot":
    print(auto1.get_info())
    print(auto1.pujc_auto())
elif znacka_auta == "Škoda":
    print(auto2.get_info())
    print(auto2.pujc_auto())
else:
    print("Špatně zadaná značka vozidla.")







