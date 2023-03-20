def carpim():
    soru = int(input('Kac sayi carpacaksiniz?')) 
    sayilar = []
    for i in range(1, soru+1):
        sayi = int(input('{}. sayiyi giriniz: '.format(i)))
        sayilar.append(sayi)
    carp = 1
    for j in sayilar:
        carp *= j
    
    return carp