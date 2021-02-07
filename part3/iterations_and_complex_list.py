import os, functools ,operator
# Dowolny obiekt obsługujący metodę __next__() przechodzącą do kolejnego 
# wyniku ,który zgłasza wyjątek StopIteration na końcu serii wyników 
# nazywamy iteratorem i można je ogarnąć pętlą for 

#467 Ten interfejs jest mniej więcej tym...

#iterowanie po pliku odbywa się wg. wierszy
for line in open('mydata.txt'):
    print(line,end='')
#to jest najlepsza ,najprosztsza i najszybsza metoda wczytywania plików
#lepiej działa pod kątem wykorzystania pamięci , nie warto wczytywać od razu
#całegu pliku ,gdyż może jej zabraknąć
#pętla for jest szybsza niż while

#ręczne sterowanie iteracją  -> wywołanie metody .next() ,która wywołuje
#metodę __next__
print('\n')

f = open('mydata.txt')
next(f)
print(f.readline())#wyświetli 'kosmos'
f.close()

#Protokół iteracji jest oparty na dwóch obiektach:
# - obiekt iterowalny ,którego metoda __iter__ jest odpalana przez funkcję iter()
# - obiekt iteratora zwracany przez obiekt iterowalny , generujący wartości
# podczas iteracji + (patrz wyżej)

#obiekt pliku jest iteratorem oraz obiektem iterowalnym
#map , zip tak samo
#i jako ,że sam w sobie jest obiektem iteracji ,to istnieje tylko jeden
#obiekt iterujący naraz

#np. dla list trzeba uzyskać iterator, może być ich kilka naraz
L = [1,2,3,4]
I1 = iter(L)
I2 = iter(L)
print(I1.__next__())
print(I1.__next__())
print(next(I2))

#ręczne iterowanie w pętli
I = iter(L)
while True:
    try:
        X = next(I)
    except StopIteration:
        break
    print(X,end=' ')
print('\n')
#iterowanie po słownikach

D = dict(kosmos=2,baran=1,helga=5)
I = iter(D)
print(next(I))
print(next(I))
#iteruje po kluczach

#tak samo za pomocą for
for key in D:
    print(key,end= ' ')
print('\n')

P = os.popen('dir')
#print(next(P)) błąd , P samo w sobie nie jest iteratorem jak plik
I3 = iter(P)
print(next(I3))
P.close()

#funkcja range nie zwraca prawdziwej listy , chociaż tak się zachowuje 
#w pętli for 

R = range(5)
print(R)
I = iter(R)
print(next(I))
print(next(I))

#Jak działa enumerate?
L = ['a','b','c']
E = enumerate(L)
I = iter(E)
print(next(I))
print(next(I))
print(next(I))

#######         LISTY SKŁADANE              

L = [1,2,3]
L = [x+10 for x in L]
print(L)
#tutaj jest tworzona nowy obiekt listy 
#listy składane są dwukrotnie wydajniejsze niż gdybyśmy tworzyli tak listę
#w pętli

#pobieranie wierszy pliku w postaci listy bez znaków \n
#po zakończeniu od razu zamyka plik
L = [line.rstrip() for line in open('mydata.txt')] # nie ładuje od razu 
#do pamięci całego pliku!!!
print(L) 

#można też taki bajer odpalić,czyli po lewej stronie mogę fajne rzeczy 
#umieścić
L = [('o' in line,line,line[0]) for line in open('mydata.txt')]
print(L)

#   Klauzula filtrująca if

L = [('o' in line,line,line[0]) for line in open('mydata.txt') 
if len(line) > 4] #jeśli predykat tutaj zostanie spełniony ,to element zostanie
#dodany do listy. Tutaj wszystkie linie dłuższe niż 4 znaki są dodawane do listy
print(L)

#bardziej rozbudowane wyrażenie
L = [('o' in line,line,line[0]) for line in open('mydata.txt') 
if line.rstrip()[-1].isdigit() ]
print(L)

#   Zagnieżdżone pętle: klauzula for
Ly = [1,2,3,4]
Lx = [5,6,7,8]

#taką instrukcję 
L.clear()
for x in Lx:
    for y in Ly:
        L.append(x+y)
print(L)
#mogę zapisać tak
L  = [x + y for x in Lx for y in Ly]#pętle idące w prawo są coraz bardziej
print(L)                            #zagnieżdżane

#użycie filtra if 
L = [x for x in [1,2,3,4,5,6,7] if x % 2 == 0]
print(L)

#użycia filtra if w liście zagnieżdżonej 
L = [(x*y,x+y) for x in [1,2,3,4,5,6,7] if x % 2 == 0 
         for y in [1,2,3,4,5,6,7] if y % 2 == 1]
print(L)

M = [[1,2,3],
     [4,5,6],
     [7,8,9]]

#iterowanie po przekątnej
L = [M[x][x] for x in range(0,3)]
print(L)

#przetwarzanie wektora macierzy
#jednak tutaj jest tworzona nowa macierz 
M = [elem*2 for row in M for elem in row] # pętle leżące po prawej stronie innych pętli mają dostęp do 
print(M)                                  # zmiennych iteracyjnych pętli po prawej stronie                                   

M = [[1,2,3],
     [4,5,6],
     [7,8,9]]

N = [[1,2,3],
     [4,5,6],
     [7,8,9]]

#psuedo-mnożenie macierzy
K = [M[row][col] * N[row][col] for row in range(3) for col in range(3)]
print(K)

#wsadzenie funkcji do listy składanej
L = [ord(x) for x in 'xd']
print(L)

#FUNKCJA map() oraz listy składane działają z wydajnością C !!!
#natomiast zwykłe pętle są wykonywane przez na maszynie wirtualnej Pythona

# Inne konteksty iteracyjne
print('Inne konteksty iteracyjne')


#funkcje-narzędzia iteracyjne 
#są dostępne też w podpiętch wyżej bibliotekach
#funkcja map() wywołuje na każdym elemencie w obiekcie iterowalnym inną
#funkcję
L = [1,2,3,4]
def op(x):
    return x **2
L = map(op,L) #zwraca listę

L = [1,2,3,4]

print(L)
L = functools.reduce(operator.add,L) #zwraca wynik operacji ,coś jak accumulate
print(L)

#niektóre funkcje wykorzystujące obiekty iterowalne
# sorted sortuje elementy obiektów iterowalnych, 
# zip łączy elementy z kilku takich obiektów, 
# enumerate wylicza elementy wraz z ich indeksem,
# filter zwraca elementy, dla których spełniony jest podany warunek,
# reduce wykonuje wskazaną funkcję na poszczególnych elementach obiektu
# iterowalnego.

#ale również zwracają obiekt iterowalny!

L = [1,2,3,4,5,6]

def pred(x):
    if x % 2 == 0: return True
    return False
L = list(filter(pred,L))
print(L)

#Przypisanie sekwencji również fajnie obsługuje obiekty iterowalne
a,b,c,*d = open('mydata.txt')
print(a,b,c,d)

#tak samo testy przynależności
print('ABBA' in open('mydata.txt'))

#przypisanie wycinka
L[1:3] = open('mydata.txt')
print(L)

#albo metoda extend() dla list
L.extend(open('mydata.txt'))
print(L)

L = [1,2,3]
L.append(open('mydata.txt')) #metoda open NIE iteruje,więc wsadza od razu
print(L)                     #cały obiekt 

#tworzenie zbiorów za pomocą iteracji
S = set(open('mydata.txt'))
print(S)

#tworzenie słowników za pomocą iteracji
D = {ix: line for ix,line in enumerate(open('mydata.txt'))}
print(D)

#dodatkowo wykorzystanie filtrów
D = {ix : line for ix,line in enumerate(open('mydata.txt')) if ix % 2 == 0}
print(D)

#dodatkowe funkcje pomocnicze pracujące na obiektach iterowalnych
L = [1,2,3,4,5,6]
print(sum(L))
print(any(L)) #jeśli którykolwiek wyraz != False zwraca True
print(all(L))
L.append(0)
print(all(L)) # jeśli wszystkie wyrazy == True zwraca True
L.append(0)
print(max(L))
print(min(L))

#rozpakowywanie kolekcji wartości do postaci poszczególnych argumentów

def fnc(a,b,c,d):
    return a+b+c+d
L = [1,2,3,4]
print(fnc(*L))

#Funkcje map,zip,filter
#funkcje te są swoimi własnymi iteratorami ,czyli nie mogę tam  przeprowadzać
#kilku iteracji jednocześnie

M = map(abs,[0,-2,-3]) #zwraca obiekt iterowalny
print(M) #to nie jest lista!

for x in M: print(x)

#iterator można przekształcić w listę
L = list(map(abs,(1,-4,-6)))
print(L)

#zip
for pair in zip((1,2,3),('1','2','3')): print(pair)

L = zip((1,2,3),('1','2','3'))
L2 = next(L)
print(L2)
L2 = next(L)
print(L2)

#filter tak samo

#Iteratory wieloktrone vs pojedyncze

R = range(4)
I1 = iter(R)
print(next(I1))
I2 = iter(R)
print(next(I1))
print(next(I2))
#omawiane wcześniej funkcje takich bajerów nie obsługują

#Widoki słowników

D = dict(a=1,b=2,c=3)
K = D.keys()
#next(K) #to nie są obiekty iterowalne
I = iter(K)
#ale mają iteratory

#ale same słowniki są obiektami iterowalnymi 
for keys in D: print(keys)




