diller = ['Python', 'R', 'Julia', 'C#', 'C++', 'C', 'Java', 'JavaScript','Matlab']

# listenin elemanlarini bastiran for dongusu
for i in diller:
    print(i)
    
print('-------------------------------')

# iterator ile ilk 3 elamani bastiralim
iterator = iter(diller)
print(next(iterator))
print(next(iterator))
print(next(iterator))

print('-------------------------------')

# iterator ile tüm listeyi yazdırmak 
iterator2 = iter(diller)
print(*iterator2)