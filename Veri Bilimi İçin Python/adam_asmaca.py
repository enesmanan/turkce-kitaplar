import random

def rastgele_kelime_tut():
    kelimeler = ['python', 'numpy', 'pandas', 'scikit-learn', 'keras', 'tensorflow', 'matplotlib', 'pytorch', 'seaborn', 'flask', 'pillow', 'deepface']
    return random.choice(kelimeler)

def asma_basamaklari(denemeler):
    adimlar = [
        '''
            +------+
            |      |
            |      O
            |     \\|/
            |      |
            |     / \\
          _===_
        ''',
        '''
            +------+
            |      |
            |      O
            |     \\|/
            |      |
            |     /
          _===_
        ''',
        '''
            +------+
            |      |
            |      O
            |     \\|/
            |      |
            |
          _===_
        ''',
        '''
            +------+
            |      |
            |      O
            |     \\|
            |      |
            |
          _===_
        ''',
        '''
            +------+
            |      |
            |      O
            |      |
            |      |
            |
          _===_
        ''',
        '''
            +------+
            |      |
            |      O
            |
            |
            |
          _===_
        ''',
        '''
            +------+
            |      |
            |
            |
            |
            |
          _===_
        '''
    ]
    return adimlar[denemeler]

def oyun():
    kelime = rastgele_kelime_tut()
    kelime_uzunlugu= len(kelime)
    tutulan_kelime = '_' * kelime_uzunlugu
    tahmin_harfleri = set()
    denemeler = 6

    print('ADAM ASMACA OYUNUNA HOS GELDINIZ!','\nYONERGE:', 
            'Programin rastgele bir sekilde tuttugu Python kutuphanesini tahmin etmeye calisin.',
            '\nNOT: Tum kelimeler kucuk harflerden olusmaktadir ve 7 adet deneme hakkin vardir.')
    
    while (denemeler > 0 or denemeler == 0) and tutulan_kelime != kelime:
        print(asma_basamaklari(denemeler))
        print(tutulan_kelime)
        print(f'Kullanilan harfler: {", ".join(tahmin_harfleri)}')

        tahmin = input('Bir harf giriniz: ').lower()

        if len(tahmin) == 1 and tahmin.isalpha():
            if tahmin in tahmin_harfleri:
                print('Bu harf zaten girildi.')
            elif tahmin in kelime:
                print('Harfi tutturdunuz!')
                tahmin_harfleri.add(tahmin)
                tutulan_kelime = ''.join([harfler if harfler in tahmin_harfleri else '_' for harfler in kelime])
            else:
                print('Bu harf tutmadi.')
                tahmin_harfleri.add(tahmin)
                denemeler -= 1
        else:
            print('Lütfen geçerli bir harf giriniz.')

    if tutulan_kelime == kelime:
        print('Tebrikler, kutuphaneyi tutturdunuz!')
    else:
        print(f'Bulamadiniz, doğru kutuphane {kelime} olacakti.')

if __name__ == '__main__':
    oyun()