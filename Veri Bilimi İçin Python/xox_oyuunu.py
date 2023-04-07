from colorama import Fore, Style

tahta = {'1': '', '2': '', '3': '',
        '4': '', '5': '', '6': '',
        '7': '', '8': '', '9': ''}

def oyun_tahtasi(tahta):
    for i in range(1, 10):
        # sayilari yerlestir
        if tahta[str(i)] == '':
            # sayilari soluk yaz
            print(Fore.LIGHTBLACK_EX + str(i) + Style.RESET_ALL, end='')
        else:
            print(tahta[str(i)], end='')
        # tabloyu ciz
        if i % 3 == 0:
            print()
            if i < 9:
                print('-+-+-')
        else:
            print('|', end='')

def kazanma_durumu(tahta, simge):
    # yan yana kazanma durumu
    if tahta['1'] == tahta['2'] == tahta['3'] == simge:
        return True
    if tahta['4'] == tahta['5'] == tahta['6'] == simge:
        return True
    if tahta['7'] == tahta['8'] == tahta['9'] == simge:
        return True

    # alt alta kazanma durumu
    elif tahta['1'] == tahta['4'] == tahta['7'] == simge:
        return True
    elif tahta['2'] == tahta['5'] == tahta['8'] == simge:
        return True
    elif tahta['3'] == tahta['6'] == tahta['9'] == simge:
        return True

    #capraz kazanma durumu
    elif tahta['1'] == tahta['5'] == tahta['9'] == simge:
        return True
    elif tahta['3'] == tahta['5'] == tahta['7'] == simge:
        return True
    
    else:
        return False #beraberlik durumu

sembol = 'X'  # ilk olarak oyuna X baslasin
oyun_tahtasi(tahta) # tahtayi yazdir
for i in range(9):
    print(sembol + ', nereye yerlestirilsin?')
    gir = input()  # sembol gir
    if tahta[gir] == '':  # girilen hucre bossa
        tahta[gir] = sembol
        if sembol == 'X':  # sembolu degistir
            sembol = 'O'
        else:
            sembol = 'X'
    else:
        print('Bu hucre zaten dolu! Lutfen baska bir hucre seciniz.')
        continue
    oyun_tahtasi(tahta)  # sembolu tahtaya yerlestir
    # sonuc ciktisi
    if kazanma_durumu(tahta, 'X'):
        print('X kazandi!')
        break
    if kazanma_durumu(tahta, 'O'):
        print('O kazandi!')
        break
# beraberlik durumu
if not kazanma_durumu(tahta, 'O') and not kazanma_durumu(tahta, 'X'):
    print('Berabere!')
