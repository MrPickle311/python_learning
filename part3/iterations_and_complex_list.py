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

#mogę również tam umieścić klauzulę if ,ale to dopiszę później
#!!! WRÓC TUTAJ W ROZDZIALE 20

# Inne konteksty iteracyjne

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

#481 Zgodnie z tym, co napisaliśmy w