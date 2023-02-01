# Položky na skladu
sklad = {
  "1N4148": 250,
  "BAV21": 54,
  "KC147": 147,
  "2N7002": 97,
  "BC547C": 10
}

polozka = input("Zadej položku: ")

if polozka in sklad:  # Zda je požadovaná položka na skladě
    print(f'Položka {polozka} je na skladě v množství {sklad[polozka]} ks.')
    mnozstvi = input("Zadej požadované množství: ") # Vložení požadovaného množství
    if int(mnozstvi) <= int(sklad[polozka]):# Kontrola množství na skladě dle požadavku
        print('Požadované množství je na skladě a objednávku lze uskutečnit v plné výši.')
        sklad[polozka] -= int(mnozstvi) # Změna množství na skladě u vybrané položky
        print(f"Položky {polozka} bylo prodáno {mnozstvi} ks.") # Celková informace o objednávce
        print(sklad) # Vypsání aktuálního stavu na skladě
    else: #Požadované množství není na skladě
        print('Požadované množství není na skladě.') 
else:  # Položka není na skladě
    print(f'Bohužel, položka {polozka} není na skladě.')