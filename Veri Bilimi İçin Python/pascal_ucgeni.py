def pascalin_ucgeni(satir_sayisi):
    liste = []
    for i in range(satir_sayisi):
        liste.append([1]) # Her satirin basina 1 ekle

        for j in range(1, i):
            # Her elemanin degeri ust satirdaki iki elemanin toplamina esittir
            eleman = liste[i-1][j-1] + liste[i-1][j]
            liste[i].append(eleman)

        # Her satirin sonuna 1 ekle
        if satir_sayisi != 0:
            liste[i].append(1)

    for i in range(satir_sayisi):
        # Satir basi bosluklari
        print('   '*(satir_sayisi-i), end=' ', sep=' ')
        # Her elemani 6 karakter genisliginde yazdir
        for j in range(0, i+1):
            print('{0:6}'.format(liste[i][j]), end=' ', sep=' ')
        print() # Daha bosluklu bir cikti icin print('\n')

    if satir_sayisi < 1:
        print('Satir sayisi en az 1 olmalidir.')
    return None

if __name__ == '__main__':
    try:
        satir_sayisi = int(input('Satir sayisini giriniz: '))
        pascalin_ucgeni(satir_sayisi)
    except ValueError as e:
        print('Satir sayisi sadece 0\'dan buyuk tamsayilardan olusabilir. ', e)


