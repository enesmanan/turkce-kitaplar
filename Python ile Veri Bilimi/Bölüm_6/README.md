## 6.3 Alıştırmalar

### Kod Açıklaması

Calisan adında bir sınıf tanımladık. Bu sınıfa, çalışanın ismi, işe giriş tarihi, unvanı ve maaşı özellikleri atadık. Çalışanların sayısını tutması için <b>toplamCalisanSayisi</b> adında bir sınıf değişkeni tanımladık. Çalışan bilgilerini ekrana bastırmak için calisan_bilgileri metodu ve çalışanın maaşına zam yapmak için <b>zam_yap</b> adlı iki metod tanımladık. 

Sınıfın özellikleri __init__ metodunda tanımlanır ve her özellik için bir değişken oluşturulur. Bir Calisan örneği oluşturulduğunda, özelliklerine __init__ metodunda verilen değerler atanır.

Örnek olarak:

<b>`calisan1 = Calisan('Enes', '10/06/2023', 'Veri Bilimci', 25000)`</b>

calisan1'in özelliklerine <b>`.`</b> operatörü ile erişilebilir ve bu özelliklerin değerleri okunabilir veya değiştirilebilir.

calisan1'in bilgilerini ekrana bastırmak için:
<b>`calisan1.calisan_bilgileri()`</b> calisan_bilgileri() metodu kullanılabilir.
