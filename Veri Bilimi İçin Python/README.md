# :blue_book: Veri Bilimi İçin Python 
Bu klasör kitaptaki ilgimi çeken örnek programların genişletilmiş ve geliştirilmiş versiyonlarını içerir. 

Kitabın isminde veri bilimi ibaresi olsa da büyük bir kısımda Python temelleri anlatılmış olduğundan dolayı veri bilimi ile doğrudan alakalı program sayısı tatminkar seviyede değil.

## :open_book: Programlar

### :point_right: [Pascal Üçgeni](https://github.com/enesmanan/turkce-kitaplar/blob/main/Veri%20Bilimi%20%C4%B0%C3%A7in%20Python/pascal_ucgeni.py)
+ Kullanıcıdan int tipinde aldığı satır sayısı inputuna göre konsola Pascal Üçgenini basar. Buradaki ana amacım gerçekten konsoldaki görüntünün orantılı bir şekilde gözükmesiydi.

### :point_right: [Rastgele Şifre Oluşturucu](https://github.com/enesmanan/turkce-kitaplar/blob/main/Veri%20Bilimi%20%C4%B0%C3%A7in%20Python/rastgele_sifre_olusturucu.py)
+ Kullanıcıdan int tipinde aldığı şifre uzunluğu inputuna göre rastgele karakterlerden oluşan bir şifre oluşturur.

**NOT:** Pascal Üçgeni ve Rastgele Şifre Oluşturucu programlarında hata ayıklama işlemini `if __name__ == '__main__':` yapısı altına yazdığım için modül olarak kullanılırsa hata ayıklama kısımları çalışmayacaktır. Hata ayıklama ksımlarının çalışmasını istiyorsak, bir main fonksiyonu oluşturup içerisinde hata ayıklama yapmak daha doğru bir yaklaşım olacaktır. Nitekim yazdığım diğer programlarda bunu tecrübe ettim.

### :point_right: [Sayısal Loto Çekilişi](https://github.com/enesmanan/turkce-kitaplar/blob/main/Veri%20Bilimi%20%C4%B0%C3%A7in%20Python/sayisal_loto.py)
+ Program her çalıştırıldığında 1 ile 49 arasındaki (49 dahil) 6 adet unique sayı üretir. 

### :point_right: [Puanlı Sayı Tahmin Oyunu](https://github.com/enesmanan/turkce-kitaplar/blob/main/Veri%20Bilimi%20%C4%B0%C3%A7in%20Python/sayi_tahmin_oyunu.py)
+ Dört adet zorluk seviyesi sunar ve bilgisayarın rastgele olarak tutmuş olduğu sayıyı oyuncu tahmin etmeye çalışır. Buradaki ana amacım oyun scorunu şaşaalı bir şekilde sunabilmekti. Bununu yapmanın yolunuda tarayıcıyı açıp raporu oyuncuya göstermeyi düşündüm. Bunun için [webbrowser](https://docs.python.org/3/library/webbrowser.html) modülünü kullandım. Daha estetik bir sonuç için HTML kısmı geliştirilebilir. 

### :point_right: [Adam Asmaca](https://github.com/enesmanan/turkce-kitaplar/blob/main/Veri%20Bilimi%20%C4%B0%C3%A7in%20Python/adam_asmaca.py)
+ Oyuncu bilgisayarın rastgele bir şekilde tuttuğu Python kütüphanesini tahmin etmeye çalışır.

### :point_right: [Ing-Tr Sözlük](https://github.com/enesmanan/turkce-kitaplar/blob/main/Veri%20Bilimi%20%C4%B0%C3%A7in%20Python/ing_tr_sozluk.py)
+ Bilmediğiniz bir ingilizce kelimeyi arayabilirsiniz. Eğer kelime [sozluk.txt](https://github.com/enesmanan/turkce-kitaplar/blob/main/Veri%20Bilimi%20%C4%B0%C3%A7in%20Python/sozluk.txt) dosyasının içinde yoksa, olmayan kelimeyi program ilk çalıştırıldığı anda otamatik olarak oluşan yeni_kelimeler.txt dosyasının içerisine, programın 2 numaralı fonksiyonu ile ekleyebilirsiniz. 

**NOT:** Programın çalışabilmesi için sozluk.txt dosyası ile programın kaynak kodlarının aynı dizinde olması gerekiyor.

### :point_right: [XOX Oyunu](https://github.com/enesmanan/turkce-kitaplar/blob/main/Veri%20Bilimi%20%C4%B0%C3%A7in%20Python/xox_oyunu.py)
+ XOX oyununu konsol üzerinden oynayabilirsiniz. Oyunda herhangi bir algoritma veya yapay zeka eşlik etmiyor, oyuncu sırası ile X ve O harflerini tahtada belirtilen yerlerden birisine koyar. 

### :point_right: [E-Posta Doğrulama](https://github.com/enesmanan/turkce-kitaplar/blob/main/Veri%20Bilimi%20%C4%B0%C3%A7in%20Python/email_dogrulama.py)
+ Regex ile girilen e-postanın doğruluğu kontrol edilir. E-postaların içerisinde "." dışında özel karakterler bulunamayacağı için eğer özel karakter girildiyse onları kaldırarak girilen e-postayı tahmin etmeye çalışır.

### :point_right: [Datetime Uygulamaları](https://github.com/enesmanan/turkce-kitaplar/blob/main/Veri%20Bilimi%20%C4%B0%C3%A7in%20Python/datetime_uygulamalar.py)
+ Datetime modülünü öğrenebilmek için çeşitli-ufak programların bir araya getirilmesinden oluşur. Program ile iki tarih arasındaki farkı bulmak, doğum gününe kaç gün kaldığını görmek, takvimi görüntülmek, istenilen ülkenin saatini görmek, tatil ve bayram günlerine kaç gün kaldığını öğrenmek gibi şeyler yapılabiliyor.

**NOT:** Bu programı exe formatına getirdim, dileyenler [buradaki](https://drive.google.com/drive/folders/1t2TfsGxblBPyYrzBzz2RuYUcErF3ksvw?usp=sharing) adresten sağ yukarıdan tümünü indir deyip ***dist*** klasörünün içerisindeki ***run.exe*** dosyasını çalıştırarak, kendi bilgisayarında Python kurulu olmasa bile programı deneyimleyebilirsiniz.  

### :point_right: [IMDB Top 250](https://github.com/enesmanan/turkce-kitaplar/blob/main/Veri%20Bilimi%20%C4%B0%C3%A7in%20Python/imdb_veri_cekme.py)
+ Bu program IMDB sitesinde top 250 olarak gözüken filmlerin bilgilerini çeker akabinde bir csv dosyası oluşturur ve bilgileri içerisine yazar.

### :point_right: [Twitter Veri Çekme](https://github.com/enesmanan/turkce-kitaplar/blob/main/Veri%20Bilimi%20%C4%B0%C3%A7in%20Python/twitter_veri_cekme.py)
+ Twitter'an veri çekmenin birçok farklı yolu mevcuttur. Bu programı kodlarken ben de kitapta gösterilen [pytwitterscraper](https://github.com/mrwan200/pytwitterscraper) isimli modülü kullandım. Program ile Türkiye'deki ve diğer ülkelerdeki trend konuları görebilmek, kullanıcı adı veya ID'si girilen kişinin profil bilgilerine ulaşmak, bir tweetin bilgilerini veya yorumlarını görmek, girilen kullanıcı adını kullanan diğer kişileri görüntülemek ve kullanıcı adı bilinen bir kişinin ID bilgisine ulaşmak gibi işlemler yapılabilir. 

**NOT:** Maalesef tweet çekme işlemini bu paket ile yapamıyoruz. Tahminimce Elon Musk'ın Twitter'ı satın almasından sonra değişen politikalar ile alakalı. (Tweet çekmek için [Tweepy](https://docs.tweepy.org/en/stable/) kütüphanesi kullanılabilir.)

### :point_right: [OpenCV Uygulamaları](https://github.com/enesmanan/turkce-kitaplar/blob/main/Veri%20Bilimi%20%C4%B0%C3%A7in%20Python/opencv_uygulamalari.py)
+ Kullanıcının bilgisayarından seçtiği bir resme döndürme, grileştirme ve blur atma gibi işlemler yapılabiliyor. 

**NOT:** Bu programın çalışabilmesi için resmin bulunduğu dosya yolunda Türkçe karakter bulunmaması gerekiyor. Yani bilgisayarınızı Türkçe olarak kullanıyorsanız dosya yolunda Masa Üstü bulunabilir. Bu durumda dosya yolu Türkçe karakter içerdiği için program çalışmayacaktır.
