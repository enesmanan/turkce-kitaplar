from random import randint
import webbrowser

def sayi_tahmin_oyunu():
    print('----------------------------------------------')
    print('            SAYI TAHMIN OYUNU')
    print('----------------------------------------------')
    print()

    oyun = True
    puan = 0
    rapor = []

    while oyun:
        print()
        x = int(input('''Level seciniz:
        Kolay icin 1 (1-10)
        Orta icin 2  (1-50)
        Zor icin 3   (1-100)
        Cok zor icin 4 (1-1000)'e basiniz: '''))

        if (x == 1):
            i = randint(1,10)
            hak = 5

        elif (x == 2):
            i = randint(1,50)
            hak = 6

        elif (x == 3):
            i = randint(1,100)
            hak = 7

        elif (x == 4):
            i = randint(1,1000)
            hak = 8

        else:
            print('Lutfen 1 ile 5 arasinda sayi giriniz.')
            break

        while True:

            if hak > 0:
                try:
                    tahmin = int(input('Sizce sayi kactir? \n'))
                except ValueError:
                    print('Lutfen bir tam sayi giriniz.')
                    continue
            else:
                print('Sayiyi tahmin edemediniz: Sayi : {}'.format(i))
                rapor.append(f'<tr><td>{x}</td><td>{puan}</td><td>Kaybettiniz</td></tr>')
                break
            if tahmin != i:
                hak -= 1
                if tahmin > i:
                    print('Sayi asagida, kalan tahmin hakkiniz : {}'.format(hak))
                else:
                    print('Sayi yukarida, kalan tahmin hakkiniz : {}'.format(hak))
            else:
                print('Tebrikler, sayiyi buldunuz.')
                puan += hak
                rapor.append(f'<tr><td>{x}</td><td>{puan}</td><td>Kazandiniz</td></tr>')
                break

        devam = input('Oyuna devam etmek istiyor musunuz? (E/H)')

        if devam == 'E' or devam == 'e':
            oyun = True
        else:
            oyun = False
    
    return rapor


def oyun_raporu_html():
    rapor = sayi_tahmin_oyunu()
    html = f'''
    <html>
        <head>
            <title>Oyun Raporu</title>
        </head>
        <body>
            <table>
                <tr>
                    <th>Level</th>
                    <th>Puan</th>
                    <th>Durum</th>
                </tr>
                {''.join(rapor)}
            </table>
        </body>
    </html>
    '''
    with open('oyun_raporu.html', 'w') as file:
        file.write(html)
    webbrowser.open_new_tab('oyun_raporu.html')
    

if __name__ == '__main__':
    oyun_raporu_html()
