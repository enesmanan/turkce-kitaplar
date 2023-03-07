import numpy as np

def sirala(dizi):
    for i in range(len(dizi)):
        min_index = i+ np.argmin(dizi[i:])
        dizi[i], dizi[min_index] = dizi[min_index],dizi[i]
    return dizi


# argmin metodu kullanmadan
def sirala2(dizi):
    for i in range(len(dizi)):
        min_index = i
        for j in range(i+1, len(dizi)):
            if dizi[j] < dizi[min_index]:
                min_index = j
        dizi[i], dizi[min_index] = dizi[min_index], dizi[i]
    return dizi
