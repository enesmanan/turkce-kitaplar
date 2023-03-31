import string
import random

# ozel karakterlerin de eklenmis hali ile
# maksimum 94 haneli bir sifre uretebilir

def sifre_olustur(uzunluk, ozel_karakterler=True):
    kucuk_harfler = string.ascii_lowercase 
    buyuk_harfler = string.ascii_uppercase
    rakamlar = string.digits

    if ozel_karakterler: # printable ile hepsi eklenebilir
        ozel_karakterler = string.punctuation
    else:
        ozel_karakterler = ''    

    karakter_listesi = [] 
    karakter_listesi.extend(list(kucuk_harfler)) 
    karakter_listesi.extend(list(buyuk_harfler)) 
    karakter_listesi.extend(list(rakamlar)) 
    karakter_listesi.extend(list(ozel_karakterler)) 
    random.shuffle(karakter_listesi) 
    
    password = ''.join(random.sample(karakter_listesi, uzunluk)) 
    return password

if __name__ == '__main__':
    while True:
        try:
            password_uzunlugu = int(input('Sifre uzunlugu giriniz: '))
            if password_uzunlugu <= 0:
                raise ValueError
            break
        except ValueError:
            print('Lutfen pozitif bir tamsayi giriniz.')
                
    ozel_karakterler = input('Ozel karakterler kullanilsin mi? (E/H): ')
    
    if ozel_karakterler.lower() == 'e':
        ozel_karakterler = True
    else:
        ozel_karakterler = False
    
    password = sifre_olustur(password_uzunlugu, ozel_karakterler)
    print('Uretilen sifre:', password)