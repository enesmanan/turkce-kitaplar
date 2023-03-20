def fibonacci(n):
    if (n <= 0):
        print('Lutfen 0\'dan buyuk bir tamsayi giriniz.')

    elif (n == 2 or n == 1):
        return 1
    else:
        return fibonacci(n-1) + fibonacci(n-2)
    
n = int(input("Sira sayisini (n) giriniz:"))
sonuc = fibonacci(n)
print("Sira sayisi: ", sonuc)