import numpy as np

# dizideki en buyuk 3 elamani buldurma
dizi = np.array([1, 3, 5, 123, 0, 999, 1, 8, 6])

sec1 = np.sort(dizi)[-3:]

# matristeki en buyuk 3 elemani buldurma
matris = np.array([[1, 3, 5],
                    [123, 0, 999],
                    [1, 8, 6]])

boyut_dusur = matris.flatten()

sec2 = np.sort(boyut_dusur)[-3:]

print(sec1)
# [8 123 999]

print(sec2)
# [8 123 999]