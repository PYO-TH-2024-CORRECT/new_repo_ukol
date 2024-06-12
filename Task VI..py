def mocnina_prvku(seznam, vykon):
    # Vytvoření nového seznamu, kde každý prvek je umocněn danou hodnotou výkonu
    vysledky = [prvek ** vykon for prvek in seznam]
    # Vrácení nového seznamu
    return vysledky

# Příklad použití funkce
seznam_cisel = [1, 2, 3, 4, 5]
vykon = 2
vysledek = mocnina_prvku(seznam_cisel, vykon)
print(f"Seznam po umocnění na {vykon}: {vysledek}")
