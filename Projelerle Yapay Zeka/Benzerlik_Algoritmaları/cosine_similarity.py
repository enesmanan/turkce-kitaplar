import re

stop_words = ['acaba', 'ama', 'ancak', 'artık', 'asla', 'aslında',
              'az', 'bana', 'bazen', 'bazı', 'belki', 'ben', 'beni',
              'benim', 'beri', 'bile', 'bir', 'biri', 'birkaç', 'birçok',
              'şey', 'daha', 'az', 'gene', 'gibi', 'da', 'de', 'en', 'daha',
              'diğer', 'diğeri', 'diye', 'dolayı', 'fakat', 'falan', 'filan',
              'gibi', 'hala', 'hatta', 'ise', 'kim', 'kime', 'niye', 'oysa', 'pek',
              'rağmen', 'sanki', 'şayet', 'sen', 'siz', 'tabii', 've', 'veya', 'zira']

# kelime stop_words'te var mi
# True/False
def stop_word(kelime):
    kelime = kelime.lower()
    return kelime in stop_words

# cumlelerdeki uniqe kelimeleri bul
def kelime_sozluk(cumleler):
    sozluk = set()
    for cumle in cumleler:
        kelimeler = cumle.split(' ')
        for kelime in kelimeler:
            kelime = re.sub(r'[^\w\s]', '', kelime)
            if kelime.lower() not in stop_words:
                sozluk.add(kelime.lower())
    return list(sozluk)

# kelime vektorlerini hesapla
def cumle2Vec(cumle, sozluk):
    vector = [0] * len(sozluk)
    kelimeler = cumle.split(' ')
    for kelime in kelimeler:
        kelime = re.sub(r'[^\w\s]', '', kelime)
        kelime = kelime.lower()
        if kelime in sozluk:
            index = sozluk.index(kelime)
            vector[index] += 1
    return vector

# noktasal carpim
def dot_product(vector1, vector2):
    if len(vector1) != len(vector2):
        raise ValueError('Vektorlerin uzunluklari esit olmalidir.')

    toplam = 0
    for i in range(len(vector1)):
        toplam = toplam + vector1[i] * vector2[i]
    return toplam

# vektor buyuklugu
def vector_magnitude(vector):
    toplam = 0
    for i in range(len(vector)):
        toplam = toplam + (vector[i] * vector[i])
    return toplam ** (1/2)

# kosinus benzerligini hesapla
def calculate_cosine_similarity(vector1, vector2):
    magnitude1 = vector_magnitude(vector1)
    magnitude2 = vector_magnitude(vector2)

    if magnitude1 == 0 or magnitude2 == 0:
        return 0

    return dot_product(vector1, vector2) / (magnitude1 * magnitude2)

if __name__ == '__main__':
    cumle_1 = 'Sokrates bir Antik Yunan filozofudur'
    cumle_2 = 'Sokrates Antik Yunanda doğmuş ve yaşamıştır'

    sozluk = kelime_sozluk([cumle_1, cumle_2])

    cumle_1_vector = cumle2Vec(cumle_1, sozluk)
    cumle_2_vector = cumle2Vec(cumle_2, sozluk)

    benzerlik_orani = calculate_cosine_similarity(cumle_1_vector, cumle_2_vector)

    print(f'Benzerlik orani {benzerlik_orani}')
