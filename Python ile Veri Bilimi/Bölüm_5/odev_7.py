A = dict(zip(('f', 'e', 'h', 'm', 'i'), (1,2,3,4,5)))
print(A) # {'f': 1, 'e': 2, 'h': 3, 'm': 4, 'i': 5}

B = range(10)
print(B) # range(0, 10)

C = sorted([A[i] for i in A])
print(C) # [1, 2, 3, 4, 5]

D = [i for i in B if i in C]
print(D) # [1, 2, 3, 4, 5]

E = {i:i*i for i in B}
print(E) # {0: 0, 1: 1, 2: 4, 3: 9, 4: 16, 5: 25, 6: 36, 7: 49, 8: 64, 9: 81}

F = [[i, i*i] for i in B]
print(F) # [[0, 0], [1, 1], [2, 4], [3, 9], [4, 16], [5, 25], [6, 36], [7, 49], [8, 64], [9, 81]]