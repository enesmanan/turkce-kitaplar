import re

stop_words = ['acaba', 'ama', 'ancak', 'artık', 'asla', 'aslında',
            'az', 'bana', 'bazen', 'bazı', 'belki', 'ben', 'beni',
            'benim', 'beri', 'bile', 'bir', 'biri', 'birkaç', 'birçok',
            'şey', 'daha', 'az', 'gene', 'gibi', 'da', 'de', 'en', 'daha',
            'diğer', 'diğeri' , 'diye', 'dolayı', 'fakat', 'falan', 'filan',
            'gibi', 'hala', 'hatta', 'ise', 'kim', 'kime', 'niye', 'oysa', 'pek',
            'rağmen', 'sanki', 'şayet', 'sen', 'siz', 'tabii', 've', 'veya', 'zira']

# kelime stop_words'te var mi
# True/False
def stop_word(kelime):
    kelime = kelime.lower()
    return kelime in stop_words

# baska dizi icin
# yardimci fonksiyon
def ara(dizi, kelime):
    return kelime in dizi

# cumlelerdeki uniqe kelimeleri bul
def kelime_sozluk(cumle):
    sozluk = []
    for kelime in cumle: 
        kelimeler = kelime.split(' ')  
        for kelime in kelimeler:  
            kelime = re.sub(r'[^\w\s]', '', kelime)  
            if kelime.lower() not in stop_words and kelime.lower() not in sozluk:
                sozluk.append(kelime.lower())
    return sozluk

# kelime vektorlerini hesapla
def cumle2Vec(cumle, sozluk):
    vector = []

    kelimeler = cumle.split(' ')
    for sozcuk in sozluk:
        sozcukSayi = 0
        for kelime in kelimeler:
            if kelime == sozcuk:
                sozcukSayi += 1
        vector.append([sozcuk, sozcukSayi])

    return vector

# noktasal carpim
def dot_product(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError('Vektorlerin uzunluklari esit olmalidir.')

    toplam = 0
    for i in range(len(vector1)):
        toplam = toplam + vector1[i][1] * vector2[i][1]
    return toplam

# vektor buyuklugu
def vector_magnitude(vector):
    toplam = 0
    for i in range(len(vector)):
        toplam = toplam + (vector[i][1] * vector[i][1])

    return toplam ** (1/2)

# kosinus benzerligini hesapla
def calculate_cosine_similarity(vector1, vector2):
     return dot_product(vector1,vector2)  / ( vector_magnitude(vector1) * vector_magnitude(vector2) )


if __name__ == '__main__':
    cumle_1 = 'Şu tarlaya bi şinik kekere mekere ekmişler.'
    cumle_2 = 'Bu tarlaya da bi şinik kekere mekere ekmişler.'

    print('1.Cümle :', cumle_1)
    print('2.Cümle :', cumle_2)

    sozluk = kelime_sozluk([cumle_1,cumle_2])

    print(sozluk)
    cumle_1_vector = cumle2Vec(cumle_1,sozluk)
    cumle_2_vector = cumle2Vec(cumle_2,sozluk)

    print(cumle_1_vector)
    print(cumle_2_vector)

    benzerlik_orani = calculate_cosine_similarity(cumle_1_vector, cumle_2_vector)

    print(f'Benzerlik orani {benzerlik_orani}')


