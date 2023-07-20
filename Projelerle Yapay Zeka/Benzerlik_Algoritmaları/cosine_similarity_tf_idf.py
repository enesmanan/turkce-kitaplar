import re
import math 
import numpy as np

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
        idf = math.log(idf_boyut / deger+1)
        idf_values[anahtar] = idf
    return idf_values

def cosine_similarity(v1, v2):
    dot_product = np.dot(v1, v2)
    norm_v1 = np.linalg.norm(v1)
    norm_v2 = np.linalg.norm(v2)
    return dot_product / (norm_v1 * norm_v2)

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

    print('\n---------------------------\n')
    tfidf_vectors = np.array([list(tf_values.values()), list(idf_values.values())])
    cosine_sim = cosine_similarity(tfidf_vectors[0], tfidf_vectors[1])
    print(f'Kosinüs Benzerliği: {cosine_sim}')

if __name__ == '__main__':
    dokuman = ['Platon\'un devletinde kişinin başkasına değil, kendisine köle olma düşüncesi vardır.',
               'Platon\'un devlet eserinde başka birisine köle olmaktansa insanın kendisine köle olma düşüncesi vardır.']
    main(dokuman)