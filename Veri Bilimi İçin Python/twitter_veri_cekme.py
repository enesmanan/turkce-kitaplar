from pprint import pprint
from pytwitterscraper import TwitterScraper

tw = TwitterScraper()


def tr_trend_konular(code='TR'):
    tt = tw.get_trends(code=code)
    for i, trend in enumerate(tt.contents[:10], 1):
        print(f"{i}. {trend['name']}")

# imput str-iso 3166 ulke kodlari
def trend_konular(code):
    tt = tw.get_trends(code=code)
    for i, trend in enumerate(tt.contents[:10], 1):
        print(f"{i}. {trend['name']}")

# input str
def profil(name):
    pr = tw.get_profile(name=name)
    pprint(pr.__dict__)

# input int
def profil_id(id_key):
    pr = tw.get_profile(id=id_key)
    pprint(pr.__dict__)

# calismiyor
#def tweet_cek():
#    tweets = tw.get_tweets(44196397, count=3)
#    pprint(tweets.contents)

# input int
def tweet_bilgileri(tweet_id):
    twinfo = tw.get_tweetinfo(tweet_id)
    pprint(twinfo.contents)

# imput int
def tweet_yorumlari(tweetid):
    twcomments = tw.get_tweetcomments(tweetid)
    pprint(twcomments.contents)

# input str
def kullanici_ara(kullanici_adi):
    search = tw.searchkeywords(kullanici_adi)
    pprint(search.users)

# input str
def id_bul(name):
    data = tw.get_profile(names=[name])
    for data_mem in data:
        print(data_mem.id)


def main():
    giris = int(input('''
    Merhaba!
    Turkiye'deki trend konulari gormek icin 1
    Diger ulkelerdeki trend konulari gormek icin 2
    Kullanici adi bilinen kisinin profil bilgilerini gormek icin 3
    ID bilgisi bilinen kisinin profil bilgilerini gormek icin 4
    Bir tweetin bilgilerini gormek icin 5
    Bir tweetin yorumlarini gormek icin 6
    Kullanici adi ile arama yapmak icin 7 
    Kullanicinin Twitter ID bilgisine ulaşmak icin 8'e basiniz.
    '''))

    if giris == 1:
        tr_trend_konular()
    if giris == 2:
        code = input('''İstenilen ulkenin ISO 3166 ulke kodunu giriniz: 
                        Bazi yaygin ulke kodlari    TR: Turkiye,
                                                    US: Amerika Birlesik Devletleri,
                                                    GB: Ingiltere,
                                                    DE: Almanya,
                                                    FR: Fransa,
                                                    JP: Japonya,
                                                    CN: Cin,
                                                    RU: Rusya''')
        trend_konular(code)
    if giris == 3:
        name = input('Twitter kullanici adiniz giriniz: ')
        profil(name)
    if giris == 4:
        id_key = input('Kullanicinin ID bilgisini giriniz: ')
        profil_id(id_key)
    if giris == 5:
        tweet_id = int(input('Tweet\'in ID bilgisini giriniz: '))
        tweet_bilgileri(tweet_id)
    if giris == 6:
        tweetid = int(input('Tweet\'in ID bilgisini giriniz: '))
        tweet_yorumlari(tweetid)
    if giris == 7:
        kullanici_adi = input('Aramak istediginiz kullanici adini giriniz: ')
        kullanici_ara(kullanici_adi)
    if giris == 8:
        name = input('ID bilgisine erismek istediginiz kullanici adiniz giriniz: ')
        id_bul(name)

if __name__ == '__main__':
    main()