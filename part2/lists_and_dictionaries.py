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

#powtórzenie elementów listy
K = L1 * 3   
print(K)

#powtórzenie list
V = [L1] * 3
print(V)

#zauważ ,że tutaj V składa się z 3 referencji do listy L

L1[1] = 0

print(V)

#tworzenie kopii zamiast referowania do elementów innej listy

V = [list(L1)] * 4 # tutaj zostaną stworzone 4 referencje do kopii L1

print(V)

L1[1] = 99

print(V) # teraz V nie zostanie zmieniona

V[0][1] = 99

print(V) # lecz teraz każdy element V zostanie zmieniony

#tworzenie prawdziwych kopii

V = [list(L1) for x in range(4) ] # tutaj każda z zagnieżdżonych list jest niezależną kopią L1

L1 = 10000
V[0][1] = 'xd'

print(V)

#w przypadku konkatencji ,czy powtórzenia dostajemy nową listę

#Iteracja, przynależność

print('Iteracja i przynaleznosc')

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

#Słownik tworzenie
print('Tworzenie slownika')

D = {'name' : 'Adam' , 'age' : 30}

D = dict([('oh no','45'),('kwargs','xd')])
print(D) # słownik można stworzyć z listy krotek

D = dict.fromkeys(['a','b','c'],6)
print(D) #tworzy słownik z kluczami a,b,c ,które wszystkie mają wartość 6

D = dict(name = 'Adam' ,age = 40)
print(D)

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
# przekształcić na listy, ale same w sobie (obiekty iterowalne) nie 
# obsługują operacji typowych dla list np. indeksowania
# ale obsługują dużo operacji typowych dla zbiorów oprócz metody values
# widok items() można traktować jako zbiór tylko wtedy ,gdy zawiera
# wyłącznie elementy niemutowalne

N = G.keys()
M = E.keys()

print(N | M) # suma zbiorowa kluczy

O = G.copy()
print(O) # Kopiowanie

if O == G:
    print('Slowniki sa sobie rowne!')

G.clear() # Czyszczenie

print(G)

G = {'aleks' : 'mohr' , 'nr' : 23}
D = {'aleks': 'Hrjalson' , 'figure' : 'brillant'}

G.update(D) # Wywołanie tej metody łączy klucze i wartości dwóch słowników
#i po prostu ślepo nadpisuje odpowiednie wartości w przypadku kolizji
#kluczy

print(G)

print(G.get('nr'))                  # znajduje wartość pod kluczem lub zwraca
print(G.get('offtop','not found!')) # wartość podaną jako drugi argument
                                    # domyślnie none

print('Usuwanie')

print(G.pop('nr'))
#metoda pop usuwa wpis o zadanym kluczu oraz zwraca jego wartość
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

#po słowniku można iterować po kluczach, ale kolejność iteracji 
#może być  losowa

print('Iterowanie po slowniku!!!')

table = {'1975': 'Monty Python i Swiety Graal', # klucz:wartość
 '1979': 'Zywot Briana',
 '1983': 'Sens zycia wedlug Monty Pythona'}

for year in table:
    print('Year : ' + year)

#odwrócenie kluczy i wartości 

keyslist = list(table.keys())
valuelist = list(table.values())

inversed_table = dict(zip(valuelist,keyslist))

for key in table.keys(): # tutaj pętla przekształca sobie obiekt iterowalny
    print(key)           # na listę

for name in inversed_table:
    print('Name : ' + name)

#ale iterować można jednocześnie klucze i wartości

for (name,year) in inversed_table.items():
    #tutaj musimy uzyc inversed_table.items()
    #gdyż items zwraca krotki
    print("Film : " + name + " was made in " + year )

#szybsza wersja

print('Szybsza wersja')
for name in table:
    print("Film : " + table[name] + " was made in " + name )

###UWAGI

#Na słownikach nie działają operacje sekwencyjne.
#Przypisanie do nowych indeksów dodaje wpisy
#Klucze nie zawsze muszą być łańcuchami znaków
#By użyć klasy zdefiniowanej przez użytkownika trzeba specjalnie 
#skonstruować klasę
#Obiekty mutowalne, takie jak listy, zbiory i inne słowniki, nie
#mogą być kluczami, ale są dozwolone jako wartości

#Słowniki mogą emulować tablice rzadkie

D = {}
D[99] = 45
D[(45,2,18)] = 22 #tutaj cała krotka jest kluczem
print(D)
print(D[(45,2,18)])

#tutaj przy sprawdzaniu i pobieraniu wartości należy użyć get i pop

#Słowniki składane

L1 = [1,2,3]
L2 = [4,5,6]

H = {k : k**3 for k in [2,3,4,5]} # zamiast listy można wstawić dowolny
                                  # obiekt iterowalny
print(H)

H = {k :v for (k,v) in zip(L1,L2)}
print(H)

#pytanka i ćwiczonka

#1.
L = list([0,0,0,0,0])
L = [0 for x in range(5)]

#2.
D = dict(a = 0,b =  0)
D = {'a' : 0,'b': 0} 


