dersler = ['Matematik', 'Fizik', 'Kimya']
ogretmenler = ['Cahit Arf', 'Mete Atatüre', 'Aziz Sancar']

ders_ogretmen = zip(dersler, ogretmenler)

for sira, cift in enumerate(ders_ogretmen):
    print(f'Ders No {sira}: Ders: {cift[0]}, Ogretmen: {cift[1]}')