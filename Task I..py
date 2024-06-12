def soucin_prvku(seznam):
    # Inicializace proměnné pro součin s hodnotou 1
    soucin = 1
    
    # Procházení všech prvků v seznamu
    for cislo in seznam:
        # Vynásobení aktuálního součinu dalším prvkem
        soucin *= cislo
    
    # Vrácení výsledného součinu
    return soucin

# Příklad použití funkce
seznam_cisel = [2, 3, 4, 5]
vysledek = soucin_prvku(seznam_cisel)
print(f"Součin prvků ze seznamu {seznam_cisel} je {vysledek}")
