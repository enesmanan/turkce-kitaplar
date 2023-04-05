import os

sozluk = {}

# yeni_kelimeler.txt dosyasini olusturmak icin
def bos_dosya_olustur(dosya_adi):
    if os.path.exists(dosya_adi): # dosya zaten varsa
        return
    with open(dosya_adi, 'w') as f:
        pass

def sozluk_arama(kelime):
    if kelime in sozluk:
        return sozluk[kelime]
    else:
        return 'Kelime bulunamadi'
    
# sozluge kelime ekle
# sozlukte kelime yoksa yeni kelimelere ekle
def sozluk_ekle(ingilizce, turkce):
    if ingilizce not in sozluk:
        sozluk[ingilizce] = turkce
        with open('yeni_kelimeler.txt', 'a', encoding='utf-8') as dosya:
            dosya.write(f'\n{ingilizce}:{turkce}')
        print(f'{ingilizce.capitalize()} kelimesi basariyla eklendi.')
    else:
        print('Bu kelime zaten sozlukte var.')

def main():
  bos_dosya_olustur('yeni_kelimeler.txt')
  with open('sozluk.txt', 'r', encoding='utf-8') as dosya:
      for line in dosya:
          if ':' not in line:
              continue
          kelime, anlam = line.strip().split(':')
          sozluk[kelime.strip()] = anlam.strip()

      while True:
        secim = input('Arama yapmak icin 1, kelime eklemek icin 2, cikmak icin q\'ya basiniz: ').lower()
        if secim == '1':
            aranacak_kelime = input('Aramak istediginiz Ingilizce kelimeyi giriniz: ').lower()
            sonuc = sozluk_arama(aranacak_kelime)
            if sonuc == 'Kelime bulunamadi':
                with open('yeni_kelimeler.txt', 'r', encoding='utf-8') as dosya:
                    for line in dosya:
                        if ':' not in line:
                            continue
                        kelime, anlam = line.strip().split(':')
                        if kelime.strip() == aranacak_kelime:
                            sonuc = anlam.strip()
                            break
            print(f'{aranacak_kelime.capitalize()}: {sonuc.capitalize()}')
        elif secim == '2':
            ingilizce_kelime = input('Eklemek istediginiz Ingilizce kelimeyi giriniz: ').lower()
            turkce_kelime = input('Eklemek istediginiz Turkce kelimeyi giriniz: ').lower()
            sozluk_ekle(ingilizce_kelime, turkce_kelime)
        elif secim == 'q':
            print('Sozluk programindan ciktiniz.')
            break
        else:
            print('Gecersiz secim, lutfen tekrar deneyiniz.')

if __name__ == '__main__':
    main()