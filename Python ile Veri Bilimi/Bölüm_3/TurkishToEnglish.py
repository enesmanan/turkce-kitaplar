def cevir(metin):
    turkce_karakterler = 'çğıöşüÇĞİÖŞÜ'
    ingilizce_karakterler = 'cgiosuCGIOSU'
    cevrim = ''
    for karakter in metin:
        if karakter in turkce_karakterler:
            index = turkce_karakterler.index(karakter)
            cevrim += ingilizce_karakterler[index]
        else:
            cevrim += karakter
    return cevrim

