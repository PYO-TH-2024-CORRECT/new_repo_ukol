def najdi_minimum(seznam):
    # Ověření, zda je seznam neprázdný
    if not seznam:
        return None  # Pokud je seznam prázdný, vrátí None

    # Inicializace proměnné pro minimum s prvním prvkem seznamu
    minimum = seznam[0]
    
    # Procházení všech prvků v seznamu od druhého prvku
    for cislo in seznam[1:]:
        # Pokud je aktuální prvek menší než dosavadní minimum, aktualizujeme minimum
        if cislo < minimum:
            minimum = cislo
    
    # Vrácení nalezeného minima
    return minimum

# Příklad použití funkce
seznam_cisel = [5, 3, 8, 1, 9, -2, 7]
vysledek = najdi_minimum(seznam_cisel)
print(f"Minimum v seznamu {seznam_cisel} je {vysledek}")
