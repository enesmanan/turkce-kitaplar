calisma_saati = int(input('Haftalik calisma saatini giriniz: '))
saat_ucreti = int(input('Saat ucretini giriniz: '))

ucret = calisma_saati * saat_ucreti

if calisma_saati > 40:
    katma_deger = (calisma_saati - 40) * (saat_ucreti * 1.5)
    ucret = (40 * saat_ucreti) + katma_deger

print(ucret)