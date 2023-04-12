import pytz
import datetime
import calendar
from dateutil.relativedelta import relativedelta

# girilen gecmis tarih ile bugun arasindaki farki hesapla
def tarih_farki():
    bugun = datetime.datetime.now()
    tarih = ['yili', 'ayi', 'gunu']
    tarih_gir = []
    for i in tarih:
        giris = input(f'Lutfen {i} giriniz: ')
        tarih_gir.append(giris)
    yil, ay, gun = map(int, tarih_gir)
    tarih_gir = datetime.datetime(yil, ay, gun)
    fark = bugun - tarih_gir
    print('Girilen tarih ile bugun arasindaki fark: ', fark.days, ' gun')

def dogum_gunume_kadar():
    bugun = datetime.datetime.now()
    tarih = ['yili', 'ayi', 'gunu']
    tarih_gir = []
    for i in tarih:
        giris = input(f'Lutfen {i} giriniz: ')
        tarih_gir.append(giris)
    yil, ay, gun = map(int, tarih_gir)
    dogum_gunu = datetime.datetime(yil, ay, gun)
    if dogum_gunu.month >= bugun.month and dogum_gunu.day >= bugun.day:
        next_birthday = datetime.datetime(bugun.year, dogum_gunu.month, dogum_gunu.day)
    else:
        next_birthday = datetime.datetime(bugun.year + 1, dogum_gunu.month, dogum_gunu.day)
    kalan_gun = (next_birthday - bugun).days
    print('Dogum gunune', kalan_gun, 'gun kaldi.')

def print_calendar():
    year = int(input('Lutfen yili giriniz: '))
    print(calendar.prcal(year))


# girilen ulkeye gore yerel saati getirir
def dunya_saati():
    ulke = input('Lutfen bir ulke kodu giriniz: \nTum ulke kodlarini gormek icin \'iso\' yaziniz.')    
    if ulke == 'iso':
        iso_3166_kodlari()
    else:
        try:
            saat_dilimi = pytz.country_timezones[ulke][0]
            yerel_saat = datetime.datetime.now(pytz.timezone(saat_dilimi))
            print('su an saat', yerel_saat.strftime('%H:%M'), ':', yerel_saat.strftime('%S'), '(', saat_dilimi, 'saati)')

        except KeyError:
            print('ulke bulunamadi.')

# ulke etiketleri
def iso_3166_kodlari():
    for country_code, timezones in pytz.country_timezones.items():
        print(country_code, timezones)

def tatil_bayram():
    tatiller = {
        'Yilbasi': datetime.date(datetime.date.today().year, 1, 1), # baz tarih
        'Ulusal Egemenlik ve cocuk Bayrami': datetime.date(datetime.date.today().year, 4, 23),
        'Emek ve Dayanisma Gunu': datetime.date(datetime.date.today().year, 5, 1),
        'Ataturk\'u Anma Genclik ve Spor Bayrami': datetime.date(datetime.date.today().year, 5, 19),
        'Ramazan Bayrami': datetime.date(datetime.date.today().year, 4, 21) + relativedelta(days=1), # 1. gunu
        'Kurban Bayrami': datetime.date(datetime.date.today().year, 6, 29) + relativedelta(days=1), # 1. gunu
        'Cumhuriyet Bayrami': datetime.date(datetime.date.today().year, 10, 29)
    }

    kalan_gunler = {}
    for tatil, tarih in tatiller.items():
        if tarih >= datetime.date.today():
            kalan_gun = tarih - datetime.date.today()
            kalan_gunler[tatil] = kalan_gun.days

    if kalan_gunler:
        for tatil, kalan_gun in kalan_gunler.items():
            print(f'{tatil} tatiline {kalan_gun} gun kaldi.')
    else:
        print('Bu yil kalan bir tatil veya bayram gunu yok.')

def finaller_2023():
    ege_final_tarihi = datetime.date(2023, 6, 12)
    kalan_gun = ege_final_tarihi - datetime.date.today()
    if kalan_gun.days > 0:
        print(f'Finallere {kalan_gun.days} gun kaldi.')
    elif kalan_gun.days == 0:
        print('Bugun Ege universitesi ogrencilerinin finallerinin basladigi gundur.')
    else:
        print('2023 finalleri zaten yapildi sinavi zaten yapildi.')

def main():
    giris = int(input('''
    Iki tarih arasindaki farki hesaplamak icin 1
    Dogum gunune kac gun kaldigini gormek icin 2
    Takvimi gormek icin 3
    Istenilen ulkenin saatini gormek icin 4
    Tatil ve bayram gunlerine kac gun kaldigini gormek icin 5
    Ege 2023 finallerine kalan zamani gormek icin 6'ya basiniz.
    '''))

    if giris == 1:
        tarih_farki()
    if giris == 2:
        dogum_gunume_kadar()
    if giris == 3:
        print_calendar()
    if giris == 4:
        dunya_saati()
    if giris == 5:
        tatil_bayram()
    if giris == 6:
        finaller_2023()



if __name__ == '__main__':
    main()