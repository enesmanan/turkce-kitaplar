import random
liste = []
for i in range(0,10):
    rastgele_sayi = random.randint(-100,100)
    liste.append(rastgele_sayi)

def sirala(liste):
    liste.sort()
    return liste

print(sirala(liste))