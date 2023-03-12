ulkeler = ['Turkiye', 'Ispanya', 'Cin', 'Italya', 'ABD', 'Ekvador', 'Fas', 'Malta']

for i in ulkeler:
    if len(i) > 5:
        print(i)
        
print('---------------------------------------------')

for j in ulkeler:
    if len(j) < 5:
        j = j.replace(j,'*')
        print(j)
    else:
        print(j)
