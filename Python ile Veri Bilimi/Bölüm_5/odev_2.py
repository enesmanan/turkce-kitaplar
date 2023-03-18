def tersten_yaz(liste):
    ters_liste = []
    for kelime in liste:
        ters_kelime = kelime[::-1]
        ters_liste.append(ters_kelime)
    return ters_liste


