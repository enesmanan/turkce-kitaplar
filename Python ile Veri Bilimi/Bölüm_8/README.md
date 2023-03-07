## 8.4 Alıştırmalar
### Kod Açıklamaları
<b>Ödev1:</b> Numpy kütüphanesinin zeros metodu ile sıfırlardan ve False değerlerden oluşan 4x4 boyutunda bir numpy array oluşturduk.

<b>Ödev2:</b> 1'den 1000'e kadar olan sayilardan olusan numpy array olusturduk, bu arraydaki sayıların 18 ile tam bolunenlerini secerek ekrana bastırdık.

<b>Ödev3:</b> NumPy dizisi içerisinden en büyük 3 sayıyı seçmek için önce `np.sort()` metodu ile diziyi sıralıyoruz, akabinde sıralanmış diziden `[-3:]` ifadesi ile son 3 elemanını seçiyoruz.

Matriste seçim yapmak için extra bir işlem olarak `flatten()` metodu ile matrisin boyutunu indirgiyoruz akabinde dizi ile aynı işlemler söz konusu.

<b>Ödev4:</b> Bir dizi içerisindeki sayıları sıralayan fonksiyonu yazdık. Fonksiyonun çalışma prensibi, her iterasyonda en küçük elemanı seçerek o anki konumuna yerleştirmek ve daha sonra işlemi, kalan elemanlar üzerinde tekrarlamaktır.

Detaylı bakarsak;

1. `for` döngüsü ile dizinin eleman uzunluğunca, diziyi eleman eleman gezeriz.
2. Dizinin belirlenen aralığındaki en küçük sayının  indexini `argmin()` metodu ile buluyoruz. En küçük değerin indexini bulmak içinde `np.argmin()` metodunun sonucu, `i` değişkenine eklenir. Bu işlem her iterasyonda kalan bölüm içindeki en küçük sayının index'ini bulmak için tekrarlanır.
3. Python'daki çoklu atama özelliği ile geçici bir değişken kullanmadan döngü içindeki en küçük sayının bulunduğu index ile döngü değişkeninin değerinin yer değiştirilmesi sağlanıyor.
4. `return` anahtar kelimesi ile sıralanmış dizi döndürülüyor ve fonksiyon son buluyor.