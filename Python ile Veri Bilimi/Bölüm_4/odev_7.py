metin = input('Metni giriniz: ')

buyukHarfSayisi = 0

for harf in metin:
    if harf.isupper():
        buyukHarfSayisi += 1


buyukHarfSayisi2 = sum(1 for harf in metin if harf.isupper())


print('Metindeki buyuk harf sayisi: ', buyukHarfSayisi)
print('Metindeki buyuk harf sayisi: ', buyukHarfSayisi2)