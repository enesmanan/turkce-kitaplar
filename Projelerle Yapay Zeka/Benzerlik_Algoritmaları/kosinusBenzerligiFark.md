### Standart Optimizasyon Koşullarında Gerçeklenmiş Kosinüs Benzerliği ile TF-IDF İşlemi ile Optimize Edilmiş Kosinüs Benzerliği Arasındaki Farklar

Kelimeleri [TF-IDF](https://github.com/enesmanan/turkce-kitaplar/blob/main/Projelerle%20Yapay%20Zeka/Benzerlik_Algoritmalar%C4%B1/TF-IDF.ipynb) ile vektörleştirdiğimizde, algoritma dokumandaki kelimelere belli ağırlık değerleri atar. Dolayısıyla standart optimizasyon koşullarında gerçeklenmiş kosinüs benzerliği algoitmasına göre benzerlik oranında fark olacaktır.

TF-IDF işlemi, bir kelimenin dokümanlardaki önemini ölçer. Bu sayede, dokümana özgü ve ayırt edici kelimelerin ağırlığı artarken dokümanda sıkça geçen, genel kelimelerin ağırlığı azalır. Bu da, cümleler arasındaki benzerliği daha iyi yansıtır.

**"Sokrates bir Antik Yunan filozofudur"** ve **"Sokrates Antik Yunanda doğmuştur"** cümlelerini ele alalım. Standart olanda benzerlik oranı 0.5 çıkarken TF-IDF yönteminde (aşağıdaki kodları verilen hazır algoritma kullanılmıştır) 0.33 çıkıyor. Bunun sebebi *Sokrates* ve *Antik* kelimelerinin ortak olmasıdır. TF-IDF bu kelimelerin ağırlıklarını azaltmıştır. Bunun sonucunda daha düşük bir benzerlik oranına ulaşılmıştır.

Genel olarak iki dokümanı karşılaştırken TF-IDF yöntemi, her dokümandaki kelimelerin benzersizliğini dikkate alarak ortak kelimelerin etkisini azaltmasından dolayı daha uygun olarak kabul edilir. 

**TF-IDF ile kosinüs benzerliğinde her dokümanda uniqe geçen kelime sayısı arttıkça dokümanlar arasındaki benzerlik oranı da artacaktır.**

### Sklearn ile TF-IDF Kosinus Benzerliği 

```python
from sklearn.metrics.pairwise import cosine_similarity
from sklearn.feature_extraction.text import TfidfVectorizer

stop_words = ['acaba', 'ama', 'ancak', 'artık', 'asla', 'aslında', 'az', 'bana', 'bazen', 'bazı', 'belki',
            'ben','beni', 'bu','benim', 'beri', 'bile', 'bir', 'biri', 'birkaç', 'birçok', 'şey', 'daha',
            'az', 'gene','gibi', 'da', 'de', 'en', 'daha','diğer', 'diğeri' , 'diye', 'dolayı', 'fakat',
            'falan', 'filan', 'gibi', 'hala', 'hatta', 'ise', 'kim', 'kime', 'niye', 'oysa', 'pek',
            'rağmen', 'sanki', 'şayet', 'sen', 'siz', 'tabii', 've', 'veya', 'zira']

def preprocess(text):
    text = text.lower()
    words = text.split()
    words = [word for word in words if word not in stop_words]
    return ' '.join(words)

def cosine_similarity_tfidf(documents):
    preprocessed_documents = [preprocess(doc) for doc in documents]

    vectorizer = TfidfVectorizer()
    tfidf_matrix = vectorizer.fit_transform(preprocessed_documents)

    cosine_sim = cosine_similarity(tfidf_matrix, tfidf_matrix)
    return cosine_sim

if __name__ == '__main__':
    documents = ['Sokrates bir Antik Yunan filozofudur.',
                 'Sokrates Antik Yunanda doğmuştur.']

    similarity_matrix = cosine_similarity_tfidf(documents)
    print(similarity_matrix[0][1])
```

[Standart Kosinüs Benzerliği](https://github.com/enesmanan/turkce-kitaplar/blob/main/Projelerle%20Yapay%20Zeka/Benzerlik_Algoritmalar%C4%B1/cosine_similarity.py)

[TF-IDF Kosinus Benzerliği](https://github.com/enesmanan/turkce-kitaplar/blob/main/Projelerle%20Yapay%20Zeka/Benzerlik_Algoritmalar%C4%B1/cosine_similarity_tf_idf.py)
