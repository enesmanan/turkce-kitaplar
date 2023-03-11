sehirler = ['Ankara', 'İzmir', 'İstanbul', 'Samsun', 'Bursa', 'Çorum', 'Tekirdağ']

# extend() metodu ile listeye eleman ekleme
sehirler.extend(['Edirne', 'Aydın'])
print(sehirler)
# ['Ankara', 'İzmir', 'İstanbul', 'Samsun', 'Bursa', 'Çorum', 'Tekirdağ', 'Edirne', 'Aydın']

# Istanbul sehrinin indexini bulma
istanbul_index = sehirler.index('İstanbul')
print(istanbul_index) 
# 2

# indexini atadigimiz degisken ile listeden cikarma
sehirler.pop(istanbul_index)
print(sehirler)
# ['Ankara', 'İzmir', 'Samsun', 'Bursa', 'Çorum', 'Tekirdağ', 'Edirne', 'Aydın']

# cevir fonksiyonunun import edilisi
from TurkishToEnglish import cevir
# listeyi alfabetik sırada yazdırma
for i in range(len(sehirler)):
    sehirler[i] = cevir(sehirler[i])
sehirler.sort()
print(sehirler)
# ['Ankara', 'Aydin', 'Bursa', 'Corum', 'Edirne', 'Izmir', 'Samsun', 'Tekirdag']


