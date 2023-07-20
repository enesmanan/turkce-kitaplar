import re
import math 

stop_words = ['acaba', 'ama', 'ancak', 'artık', 'asla', 'aslında', 'az', 'bana', 'bazen', 'bazı', 'belki',
            'ben','beni', 'bu','benim', 'beri', 'bile', 'bir', 'biri', 'birkaç', 'birçok', 'şey', 'daha',
            'az', 'gene','gibi', 'da', 'de', 'en', 'daha','diğer', 'diğeri' , 'diye', 'dolayı', 'fakat',
            'falan', 'filan', 'gibi', 'hala', 'hatta', 'ise', 'kim', 'kime', 'niye', 'oysa', 'pek',
            'rağmen', 'sanki', 'şayet', 'sen', 'siz', 'tabii', 've', 'veya', 'zira']

def kelime_listesi(dokuman):
    liste = []
    for kelime in dokuman: 
        kelimeler = kelime.split(' ')
        for kelime in kelimeler:
            kelime = re.sub(r'[^\w\s]', '', kelime)
            if kelime.lower() not in stop_words:
                liste.append(kelime.lower())
    return liste

def dokuman_boyutu(liste):
    return len(liste)

def frekans(liste):
    frekans = {}
    for kelime in liste:
        if kelime in frekans:
            frekans[kelime] += 1
        else:
            frekans[kelime] = 1
    return frekans

def tf_degeri(frekans, boyut):
    tf_values = {}
    for anahtar, deger in frekans.items():
        tf = deger / boyut
        tf_values[anahtar] = tf
    return tf_values

def idf_degeri(frekans_degerleri, idf_boyut):
    idf_values = {}
    for anahtar, deger in frekans_degerleri.items():
        idf = math.log(idf_boyut / deger)
        idf_values[anahtar] = idf
    return idf_values

def main(dokuman):
    degerler = kelime_listesi(dokuman)
    boyut = dokuman_boyutu(degerler)
    
    frekans_degerleri = frekans(degerler)
    
    print('\nTF degerleri:\n')
    tf_values = tf_degeri(frekans_degerleri, boyut)
    for kelime, tf in tf_values.items():
        print(f'{kelime}: {tf}')
    
    print('\n---------------------------\n')
    print('IDF degerleri:\n')
    idf_boyut = len(dokuman)
    idf_values = idf_degeri(frekans_degerleri, idf_boyut)
    for kelime, idf in idf_values.items():
        print(f'{kelime}: {idf}')

    print('\n---------------------------\n')
    print('TF-IDF degerleri:\n')
    for kelime in frekans_degerleri:
        tf_idf = tf_values[kelime] * idf_values[kelime]
        print(f'{kelime}: {tf_idf}')

if __name__ == '__main__':
    dokuman = ['Platon\'un devletinde kişinin başkasına değil, kendisine köle olma düşüncesi vardır.',
               'Platon\'un devlet eserinde başka birisine köle olmaktansa insanın kendisine köle olma düşüncesi vardır.']
    main(dokuman)
