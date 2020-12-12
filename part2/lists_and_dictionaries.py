#listy i słowniki są mutowalne

#LISTY
###########OPERACJE NA LISTACH#######################

#Pusta lista
L = [] 

#Cztery elementy — indeksy od 0 do 3
L = [123, 'abc', 1.23, {}] 
print(L)

#Zagnieżdżone podlisty
L = ['Adam', 40.0, ['dev', 'mgr']] 
print(L)

#Lista elementów obiektu iterowanego
L = list('mielonka')
print(L)

#)Lista kolejnych liczb całkowitych
L = list(range(-4, 4))
print(L)

#Indeks,
i = 1
j = 1
print(L[i])

#indeks indeksu,
L = [L,L] 
print(L[i][j]) 

#wycinek, 
print(L[i:j])

#długość
print(len(L))

# Konkatenacja, 
L1 = [2,3,4]
L2 = [5,6,7]
print(L1 + L2) 

#powtórzenie
K = L * 3   
print(K)

#w przypadku konkatencji ,czy powtórzenia dostajemy nową listę

#Iteracja, przynależność
for x in L:
    print(x)
p = 3 in L
print(p)

#Metody dodawania obiektów
print('Metody dodawania obiektów')

L.append(18) # przyjmuje jeden obiekt i wstawia na końcu listy referencję
#do niego
L.extend(['xd','xd']) # przyjmuje inną listę
L.insert(i,45) #(indeks,obiekt)
print(L)

#Przeszukiwanie listy
print('Przeszukiwanie listy')

print(L.index(45)) # zwraca indeks pierwszego
#obiektu , który pasuje

print(L.count('xd')) # zwraca ilość wystąpień

#Sortowanie,odwracanie,kopiowanie ,czyszczenie
print('Sortowanie,odwracanie,kopiowanie ,czyszczenie')

L= [12,1,2,14,34,3,4,234,24,23,4]
L.sort() # domyślnie w kolejności rosnącej
print(L)

L.sort(reverse= True)# w kolejnosci malejącej
print(L)

L = ['Xd' , 'xd' , 'abba' , 'Abba' , 'BangBang']
L.sort(key = str.lower)
print(L)

#argument key tworzy funkcję jednoargumentową zwracającą wartość, która
#zostanie użyta podczas sortowania , tutaj została użyta metoda str.lower

L.reverse()
print(L)

print(L.copy()) # metoda zwraca kopię

L.clear()
print(L)

#Metody , wyrażenia ,zmniejszanie listy
print('Metody , wyrażenia ,zmniejszanie listy')

L = [ 1,2,4,0,-1,23,456,32]
L.pop() # bez argumentu usuwa z końca
print(L)

L.pop(1) # z argumentem usuwa konkretny indeks
print(L)

L.remove(23) # usuwanie konkretnego obiektu
print(L)

del L[2] # usuwanie z konkretnym indeksem
print(L)

del L[1:3] # usuwanie wycinka z listy, pamiętaj o otwartym przedziale
print(L)   # z prawej strony

#Przypisanie do indeksu , przypisanie do wycinka

print('Wycinki')

L = [2,3,4,2,1,2]
L[3] = 2000
print(L)

L[1] = [] # taka operacja nie usuwa pojedynczego elementu ,lecz
print(L)  # do elementu o tym indeksie wstawia element pusty

L[1:4] = []
print(L)

L[1:2] = ['xd','xd']
print(L)

L = [2,3,4,2,1,2]
L[1:5] = L[2:6] # najpierw wycinek z prawej strony jest kopiowany
print(L)        # a potem przypisywany do lewej, więc nie tracę informacji

#Listy składane i odwzorowania
print('Listy składane i odwzorowania')

L = [x**2 for x in range(-4,11,2)]
print(L)

L = list(map(ord,'kappa'))
print(L)

############################################################################

#między listami oraz stringami trzeba przeprowadzać konwersję

L = [1,2]
str1 = '34 56'
newstr = str1 + str(L)
newlist = L + list(str1) # każdy znak z str1 będzie w osobnej szufladce
print(newstr)
print(newlist)



########################        SŁOWNIKI           ###################

#Również przechowują referencje do obiektów

#Słowniki są nieuporządkowane z natury , nie można ich sortować
#są po utworzeniu poddawane hashowaniu

#Tworzenie pustego słownika
D = {}

#Słownik
print('Tworzenie slownika')
D = {'name' : 'Adam' , 'age' : 30}
D = dict(name = 'Adam' ,age = 40)

#Zagnieżdżanie 
print('Zagniezdzanie')

E = {'part' : D}

#Slowa kluczowe , pary klucz-wartosc, spiete pary klucz-wartosc,listy kluczy
print('Slowa kluczowe , pary klucz-wartosc, spiete pary klucz-wartosc,listy kluczy')

F = dict([('name','Adam'),('age',40)])
#tworzenie słownika z listy krotek 

#tworzenie słownika z dwóch list
keylist = ['key1','key2','key3'] #lista kluczy
valuelist = [1,2,3] # lista wartości

G = dict(zip(keylist,valuelist))

#Indeksowanie
print('Indeksowanie')

print(G['key1']) # po kluczu
print(E['part']['age']) # zagnieżdżone
# jeżeli wartość nie zostanie znaleziona to zwracany jest wyjątek

#Przynależność
print('Przynależność')
P = 'key1' in G #przynależność klucza
print(P)

#Metody
print('Metody')

print(G.keys()) # wszystkie klucze

print(G.values()) # Wszystkie wartości

print(G.items()) # Wszystkie klucze-wartości w postaci krotek

# metodu keys,values,items zwracają obiekty iterowalne , które można 
# przekształcić na listy
print(G.copy()) # Kopiowanie

G.clear() # Czyszczenie

print(G)

G = {'aleks' : 'mohr' , 'nr' : 23}
D = {'aleks': 'mohr' , 'figure' : 'brillant'}

G.update(D) # dołącza z D wszystkie pary ,których klucze nie są obecne w G

print(G)

print(G.get('nr'))                  # znajduje wartość pod kluczem lub zwraca
print(G.get('offtop','not found!')) # wartość podaną jako drugi argument
                                    # domyślnie none

G.pop('offtop','Not found!')
#usuwanie według klucza, wartości domyślne (lub błąd), gdy brak
#klucza

print(G.popitem()) #usunięcie i zwrócenie pary

print(len(G)) #ilość wpisów

key = 'aleks'
G[key] = 56
#modyfikacja wartości pod zadanym kluczem
print(G)

del G[key] # usuwanie po kluczu
print(G)

G.update({'roman': 56}) #metody tworzenia nowych kluczy
G['ford'] = 'mustang'

print(G)

L1 = list(G.keys()) # tworzenie listy z kluczy
print(L1)

L2 = list(G.values())
print(L2)

H = G.copy()

print(G.keys() & H.keys())

#Słowniki składane
R = {x: x*2 for x in range(2,8,2)}
print(R) # jak widać kluczami mogą być również obiekty innego typu 
# niż string










