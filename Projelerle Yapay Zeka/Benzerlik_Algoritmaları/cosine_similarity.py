import re

stop_words = ['acaba', 'ama', 'ancak', 'artık', 'asla', 'aslında',
            'az', 'bana', 'bazen', 'bazı', 'belki', 'ben', 'beni',
            'benim', 'beri', 'bile', 'bir', 'biri', 'birkaç', 'birçok',
            'şey', 'daha', 'az', 'gene', 'gibi', 'da', 'de', 'en', 'daha',
            'diğer', 'diğeri' , 'diye', 'dolayı', 'fakat', 'falan', 'filan',
            'gibi', 'hala', 'hatta', 'ise', 'kim', 'kime', 'niye', 'oysa', 'pek',
            'rağmen', 'sanki', 'şayet', 'sen', 'siz', 'tabii', 've', 'veya', 'zira']


def stop_word(kelime):
    kelime = kelime.lower()
    return kelime in stop_words

def ara(dizi, kelime):
    return kelime in dizi

def kelime_sozluk(cumle):
    sozluk = []
    kelimeler = cumle.split(' ')
    for kelime in kelimeler:
        kelime = re.sub(r'[^\w\s]', '', kelime)
        if not kelime in stop_words:
            sozluk.append(kelime)
    return sozluk


