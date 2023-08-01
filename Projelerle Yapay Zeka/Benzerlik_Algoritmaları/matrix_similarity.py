import cv2
import numpy as np

def matris_benzerligi(gorsel_1, gorsel_2):
    yukseklik = gorsel_1.shape[0]
    genislik = gorsel_1.shape[1]

    fark = cv2.absdiff(gorsel_1,gorsel_2)

    farklilik_oran = np.mean(fark) * 100 / 255
    print('Iki gorsel arasindaki farklilik orani :' + str(farklilik_oran))

    benzerlik_oran = 100 - farklilik_oran
    print('Iki gorsel arasindaki benzerlik orani :' + str(benzerlik_oran))

    farkMatris = np.zeros(shape=(yukseklik, genislik, 3), dtype=np.uint8)
    mask = fark <= 0
    farkMatris[mask] = 255
    farkMatris[~mask] = gorsel_2[~mask]

    cv2.imwrite('farkMatris.png',farkMatris)
    print('Iki gorsel arasindaki farkliliklar, farkMatris.png dosyasi olarak kayit edildi')

if __name__ == '__main__':
    gorsel_1 = cv2.imread('gorsel1.png')
    gorsel_2 = cv2.imread('gorsel2.png')
    matris_benzerligi(gorsel_1, gorsel_2)
