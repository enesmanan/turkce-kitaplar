# Bölüm 2 - Benzerlik Algoritmaları
## Levenshtein Distance
+ [Levenshtein Benzerlik Algoritması](https://github.com/enesmanan/turkce-kitaplar/blob/main/Projelerle%20Yapay%20Zeka/Benzerlik_Algoritmalar%C4%B1/levenshtein_distance.py)
+ İki stringin birbirine dönüşümündeki en kısa mesafeyi (minimum edit distance) bulmak için en yaygın kullanılan yöntemlerden biri Levenshtein Mesafesi olduğu için, bu algoritmaya yabancı kaynaklarda Minimum Edit Distance de denilmektedir. Ancak, minimum edit distance sadece bir metrik olduğu için, Levenshtein algoritması dışında başka yöntemler ile de bulunabilir.
+ [Ağırlıklı Levenshtein Benzerlik Algoritması](https://github.com/enesmanan/turkce-kitaplar/blob/main/Projelerle%20Yapay%20Zeka/Benzerlik_Algoritmalar%C4%B1/weighted_levenshtein_distance.py) $\to$ **Ödev_1**
  + Algoritmanın ağırlıklandırılması Türk alfabesindeki harf düzenine göre yapıldı. Klavyedeki harflerin yakınlıklarına göre de yapılabilir, o zaman bir Json dosyası yazmak gerekebilir.
+ [Spell Checker](https://github.com/enesmanan/turkce-kitaplar/blob/main/Projelerle%20Yapay%20Zeka/Benzerlik_Algoritmalar%C4%B1/spell_checker.py)
  + İngilizce için örnek bir spell checker programı eklendi. İleride Türkçe için [hunspell](https://github.com/hunspell/hunspell) kütüphanesi ile entegre çalışan bir spell checker programı kodlamayı düşünüyorum.
  + Kaynak: [https://www.youtube.com/watch?v=_nkQd9SyEpw](https://www.youtube.com/watch?v=_nkQd9SyEpw)
  
<hr style='border: 0.5px solid gray; margin: 25px 0;'>

## Vector Space Similarity
+ [Vektör Uzay Benzerlik Algoritması](https://github.com/enesmanan/turkce-kitaplar/blob/main/Projelerle%20Yapay%20Zeka/Benzerlik_Algoritmalar%C4%B1/vector_similarity.py)
+ [RGB Renk Koduna Göre En Yüksek Benzerlik Oranına Sahip Rengi Bulan Algoritma](https://github.com/enesmanan/turkce-kitaplar/blob/main/Projelerle%20Yapay%20Zeka/Benzerlik_Algoritmalar%C4%B1/rgb_similarity.py)  $\to$ **Ödev_2**
  + Algoritma, konsoldan rastgele girilen RGB renk koduna göre isimlendirilmiş renklerden en yüksek benzerlik oranına sahip 3 rengi tespit eder ve döndürür.
  + Renk kodlarını [buradaki](https://www.rapidtables.com/web/color/RGB_Color.html) siteden aldım ve toplamda 139 adet renk içeriyor.
  + Renkleri algoritma her çalıştığında RGB değerlerini normalize etmek algoritmanın time complexity değerini olumsuz etkileyebileceği için ve kullancağım tüm uzay da bu değerlerden oluştuğu için algoritmaya RGB renk kodlarını normalize ederek verdim.
  + RGB renk kodları $\to$ [RGBCodes.txt](https://github.com/enesmanan/turkce-kitaplar/blob/main/Projelerle%20Yapay%20Zeka/Benzerlik_Algoritmalar%C4%B1/RGBCodes.txt)
  + Normalize edilmiş RGB renk kodları $\to$ [RGBCodes_normalized.txt](https://github.com/enesmanan/turkce-kitaplar/blob/main/Projelerle%20Yapay%20Zeka/Benzerlik_Algoritmalar%C4%B1/RGBCodes_normalized.txt)

<hr style='border: 0.5px solid gray; margin: 25px 0;'>

## Cosine Similarity
+ [Kosinüs Benzerlik Algoritması](https://github.com/enesmanan/turkce-kitaplar/blob/main/Projelerle%20Yapay%20Zeka/Benzerlik_Algoritmalar%C4%B1/cosine_similarity.py)
+ [TF-IDF Nedir?](https://github.com/enesmanan/turkce-kitaplar/blob/main/Projelerle%20Yapay%20Zeka/Benzerlik_Algoritmalar%C4%B1/TF-IDF.ipynb)
+ [TF-IDF Algoritması](https://github.com/enesmanan/turkce-kitaplar/blob/main/Projelerle%20Yapay%20Zeka/Benzerlik_Algoritmalar%C4%B1/tf_idf.py)
+ [TF-IDF ile Kosinüs Benzerliği](https://github.com/enesmanan/turkce-kitaplar/blob/main/Projelerle%20Yapay%20Zeka/Benzerlik_Algoritmalar%C4%B1/cosine_similarity_tf_idf.py)
+ [Standart vs TF-IDF  ile Optimize Edilmiş Kosinüs Benzerliği Arasındaki Farklar](https://github.com/enesmanan/turkce-kitaplar/blob/main/Projelerle%20Yapay%20Zeka/Benzerlik_Algoritmalar%C4%B1/kosinusBenzerligiFark.md) $\to$ **Ödev_3**

<hr style='border: 0.5px solid gray; margin: 25px 0;'>

## Matrix Similarity
+ [Origin Matris Benzerliği](https://github.com/enesmanan/turkce-kitaplar/blob/main/Projelerle%20Yapay%20Zeka/Benzerlik_Algoritmalar%C4%B1/origin_matrix_similarity.py)
  + Kitaptaki kodda bazı düzeltmeler yapıldı. (eksik import eklendi ve bazı küçük düzeltmeler yapıldı)
+ [Matris Benzerliği Algoritması](https://github.com/enesmanan/turkce-kitaplar/blob/main/Projelerle%20Yapay%20Zeka/Benzerlik_Algoritmalar%C4%B1/matrix_similarity.py)
  + Matris benzerliğini hesaplamak için OpenCV kütüphanesinin içerisinde bulunan hazır fonksiyonlar kullanıldı.
+ [PIL ile Görsel Fark](https://github.com/enesmanan/turkce-kitaplar/blob/main/Projelerle%20Yapay%20Zeka/Benzerlik_Algoritmalar%C4%B1/gorsel_fark.py)
  + PIL (Pillow) kütüphanesindeki hazır fonksiyonlar ile iki görsel arasındaki farkı tespit eder ve image olarak ekrana döndürür.
+ [Toleranslı Benzerlik Algoritması](https://github.com/enesmanan/turkce-kitaplar/blob/main/Projelerle%20Yapay%20Zeka/Benzerlik_Algoritmalar%C4%B1/tolerant_similarity.py)  $\to$ **Ödev_4**
  + Algoritma, tolerans değeri büyüdükçe iki piksel arasındaki renk farkının yüksek olmasına izin verir ve benzerlik oranı artar.
+ [Tanimoto Benzerliği Nedir](https://github.com/enesmanan/turkce-kitaplar/blob/main/Projelerle%20Yapay%20Zeka/Benzerlik_Algoritmalar%C4%B1/Tanimoto_Benzerligi.ipynb) $\to$ **Ödev_5**
+ [Tanimoto Benzerlik Algoritması](https://github.com/enesmanan/turkce-kitaplar/blob/main/Projelerle%20Yapay%20Zeka/Benzerlik_Algoritmalar%C4%B1/tanimoto_similarity.py)
#### Gorseller
  + Kitaptaki görsellere ek aşağıdaki gibi farklı görseller üzerinden de denemeler yapıldı.
  + [gorsel1](https://github.com/enesmanan/turkce-kitaplar/blob/main/Projelerle%20Yapay%20Zeka/Benzerlik_Algoritmalar%C4%B1/gorsel1.png), [gorsel2](https://github.com/enesmanan/turkce-kitaplar/blob/main/Projelerle%20Yapay%20Zeka/Benzerlik_Algoritmalar%C4%B1/gorsel2.png)
