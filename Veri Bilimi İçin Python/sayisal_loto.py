from random import sample
# sample unique degerler uretir

def loto_sayilarini_uret(min_sayi, max_sayi, adet):
    return sample(range(min_sayi, max_sayi + 1), adet)

def main():
    min_sayi = 1
    max_sayi = 49
    adet = 6
    sayilar = loto_sayilarini_uret(min_sayi, max_sayi, adet)
    #sayilar.sort()
    print("Lotoyu kazanan sayilar:", sayilar)

if __name__ == "__main__":
    main()