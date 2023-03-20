# 100'e kadar olan cift sayilar uretec nesnesi ile olusturuldu
cift_sayilar = (i for i in range(101) if i % 2 == 0)

# ilk 3 elemanini ekrana bastirmak
print(next(cift_sayilar))
print(next(cift_sayilar))
print(next(cift_sayilar))
