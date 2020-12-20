from collections import namedtuple
#jest niemutowalna
#Krotki są uporządkowanymi kolekcjami dowolnych obiektów
#dostęp do krotek otrzymuje się poprzez operator inedksowania
#Krotki mają stałą długość, są heterogeniczne i można je dowolnie zagnieżdżać
#Krotki są tablicami referencji do obiektów

#Tworzenie krotek

T = ()

T = (23,)
#krotka jednoelementowa T = (23) stworzyło by liczbę całkowitą 


T = ('sad',23,dict(a = 2,b = 'sd'))
T = 'sad' , 23 , dict(a = 2,b = 'sd')

T = tuple('34')
#do argumentu funkcji trzeba podać obiekt iterowalny

#Zagnieżdżanie krotek
T = ( 12 , (23,'sd'))

#dostęp do krotek

print(T[0])

print(T[1][0])

print(T[0:2])

#Operacje 

R = (34,'fafa',43)

print(T + R)

print(3 * T)
#rozmiar krotki 

print(len(R))

#sortowanie 

T = (234,24,0,23,-1)

print(tuple(sorted(T)))
#funkcja sorted zwraca listę

L = list(T)
L.sort(reverse= True)
print(tuple(L))

#Iteracje 

for x in 3*T:
    print(T, sep= '\n')

G = [x * 2 for x in T]
print(G)


#przynależność

if 12 in T:
    print('T contains 12')

T = (23,1,2,3,2,423,23,2,0)
print(T.index(2,3))
#index(wartość_szukana, wartość _offsetu , czyli jeśli znajdę ten wynik to 
# poszukaj taki sam w odległości wartość _offsetu od pozycji obecnej
# i zwróc mi indeks tej następnej pozycji )

print(T.count(23))


#Mimo to ,że krotki są niemutowalne ,to elementy wewnątrz nich , np. listy
#są mutowalne

T = (12,23,[34,23,5,6,0,-1])
T[2].sort()

#używanie namedtuple

#pozwala na wyszukiwanie po indeksach oraz kluczach

R = namedtuple('derf',['flow','moeny','brain'])
A = R('big',123,'bigger')
print(A)

#dostęp
print(A[0])
print(A[1])
print(A[2])

print(A.flow)
print(A.brain)
print(A.moeny)

print(A._asdict()) # konwersja na słownik

#ćwiczonko 

K = (4,5,6)

K = ((0,) + K[1:3])

print(K)