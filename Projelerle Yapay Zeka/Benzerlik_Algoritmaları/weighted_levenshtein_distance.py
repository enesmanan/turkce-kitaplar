class Levenshtein:
    alfabe = 'abcçdefgğhıijklmnoöprsştuüvyz'

    def __init__(self, kelime1, kelime2):
        self.kelime1 = kelime1.lower()
        self.kelime2 = kelime2.lower()
        self.kelime1_len = len(self.kelime1)
        self.kelime2_len = len(self.kelime2)

    def normalizasyon(self, kelime):
        fark = max(self.kelime1_len, self.kelime2_len) - len(kelime)
        if fark > 0:
            kelime += ' ' * fark
        return kelime
    
    def mesafe(self):
        self.kelime1 = self.normalizasyon(self.kelime1)
        self.kelime2 = self.normalizasyon(self.kelime2)

        # mesafe matrisi
        matris = [[0 for j in range(self.kelime1_len + 1)] for i in range(self.kelime2_len + 1)]

        for i in range(self.kelime2_len + 1):
            matris[i][0] = i

        for j in range(self.kelime1_len + 1):
            matris[0][j] = j
        
        for i in range(1, self.kelime2_len + 1):
            for j in range(1, self.kelime1_len + 1):
                if self.kelime1[j-1] == self.kelime2[i-1]:
                    matris[i][j] = matris[i-1][j-1]
                else:
                    mesafe = 1  # default puan
                    if self.kelime1[j-1] in self.alfabe and self.kelime2[i-1] in self.alfabe:
                        index1 = self.alfabe.index(self.kelime1[j-1])
                        index2 = self.alfabe.index(self.kelime2[i-1])
                        diff = abs(index1 - index2)
                        if diff == 1:
                            mesafe = 0.25
                        elif diff == 2:
                            mesafe = 0.5
                        elif diff > 2:
                            mesafe = 1
                    matris[i][j] = min(matris[i-1][j-1] + mesafe,    # yer degistir
                                       matris[i-1][j] + 1,           # sil
                                       matris[i][j-1] + 1)           # ekle
        
        return matris[-1][-1] 
    
    def benzerlik(self):
        max_len = max(self.kelime1_len, self.kelime2_len)
        return (max_len - self.mesafe()) / max_len

    def __str__(self):
        return f'Agirlikli Levenshtein mesafesi: {self.mesafe()}\nBenzerlik orani: {self.benzerlik()}'

if __name__ == '__main__':
    lev = Levenshtein('a', 'c')
    print(lev)