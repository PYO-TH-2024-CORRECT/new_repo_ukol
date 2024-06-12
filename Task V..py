def slouceni_seznamu(seznam1, seznam2):
    # Sloučení dvou seznamů pomocí operátoru +
    vysledny_seznam = seznam1 + seznam2
    # Vrácení výsledného seznamu
    return vysledny_seznam

# Příklad použití funkce
seznam1 = [1, 2, 3]
seznam2 = [4, 5, 6]
vysledek = slouceni_seznamu(seznam1, seznam2)
print(f"Výsledný seznam: {vysledek}")
