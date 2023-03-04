class Calisan():

    toplamCalisanSayisi = 0

    def __init__(self, isim, iseGirisTarihi, unvan, maas):
        self.isim = isim
        self.iseGirisTarihi = iseGirisTarihi
        self.unvan = unvan
        self.maas = maas
        Calisan.toplamCalisanSayisi += 1

    def calisan_bilgileri(self):
        print('Ismi :', self.isim)
        print('Ise giris tarihi: ', self.iseGirisTarihi)
        print('Unvani:', self.unvan)
        print('Maasi:', self.maas)

    def maas_zam(self, zam):
        self.maas += zam
