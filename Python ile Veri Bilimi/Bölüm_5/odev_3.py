def birlestir(kelime1,kelime2):
    def buyuk_harf(metin):
        metin = metin.upper()
        return metin
    kelime1 = buyuk_harf(kelime1)
    kelime2 = buyuk_harf(kelime2)
    return kelime1+kelime2
