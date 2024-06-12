def odstran_cislo(seznam, cislo):
    # Počáteční hodnota počítadla odstraněných prvků
    pocet_odstranenych = 0
    
    # Použití list comprehension pro vytvoření nového seznamu bez daného čísla
    novy_seznam = [prvek for prvek in seznam if prvek != cislo]
    
    # Počet odstraněných prvků je rozdíl délek původního a nového seznamu
    pocet_odstranenych = len(seznam) - len(novy_seznam)
    
    # Aktualizace původního seznamu na nový seznam
    seznam[:] = novy_seznam
    
    # Vrácení počtu odstraněných prvků
    return pocet_odstranenych

# Příklad použití funkce
seznam_cisel = [1, 2, 3, 4, 2, 5, 2, 6]
cislo_k_odstraneni = 2
pocet = odstran_cislo(seznam_cisel, cislo_k_odstraneni)
print(f"Počet odstraněných prvků: {pocet}")
print(f"Aktualizovaný seznam: {seznam_cisel}")
