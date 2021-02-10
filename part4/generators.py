#generatory generują sekwencję wyników stopniowo, nie w jednej całości.
#nie zwracają wyniku ,tylko generator wyników
#potrafią zawieszać swoje działanie i wznawiać je sekwencyjnie
#w miarę generowania kolejnych wartości
#są swoimi własnymi iteratorami jak pliki,patrz iterations_and_complex_list.py
#pozwalają oszczędzić pamięć oraz zasoby procesora

#przykład
def gensqrt(x):
    for i in range(x):
        yield i ** 2 # po każdym yieldzie funkcja mrozi swój stan i zwraca sterowanie

for i in gensqrt(5): #generator zwraca obiekt iterowalny
    print(i)

X = gensqrt(5)
print(X)
a = next(X)
print(a)
a = next(X)
print(a)
a = next(X)
print(a)

print('\nSend!\n')

#funkcja send pozwala na przejscie do kolejnego elementu iteracji
#ale dodatkowo pozwala na komunikację z kodem funkcji i wysyłanie doń danych
def gen():
    for i in range(10):
        X = yield i # generator zwraca i czyli 0,1,2,3 itd...
        # do zmiennej X są przypisywane wartości podane poprzez send()
        #czyli po prostu wymiana informacji
        print('X is with value : ',X)

G = gen()
print(next(G)) # Jako pierwsze wywołanie musi wystąpić next(), co uruchamia generator
print(G.send(67)) # Wznowienie generatora z przekazaniem wartości

#Wyrażenia generatorów — obiekty iterowalne spotykają
#złożenia
#638

#wyrażenia generatorów ,czyli coś jak listy składane ,ale zwracany jest obiekt iterowalny zamiast listy
X = (x ** x for x in range(6))
#pożlwiość pojedynczego uzyskiwania wyników podczas iteracji

L = list(X) # stworzenie listy z obiektu iterowalnego
print(L)

X = (x ** x for x in range(6)) #reset
print(next(X))
print(next(X))
print(next(X))

X = (x ** x for x in range(6)) #reset

for x in X:
    print(x)

s = 'string and '.join(x.upper() for x in  'aaa,bbb,ccc'.split(',')) # wyrażenie generatora w funkcji
#metoda join() odpala generator
#jeśli podajemy jako argument do funkcji tylko wyrażenie generatora ,to nawiasy () są zbędne
print(s)
print(sorted((x for x in s),reverse=True)) # tutaj nawiasy są już konieczne

#Wyrażenia generatora a funkcja map
#640

#zagnieżdżone listy,generatory oraz funkcje map - porównanie
L = [x * 2 for x in [x / 2 for x in (1,5,54,32,54,32,2)]]
print(L)
L = list(map(lambda x: x * 2,map(abs,[-2,5,-23,9,0])))
print(L)
L = list((x * 2 for x in [x ** 3 for x in [1,2,3,4]]))
print(L)

#do generatorów można również dać filter

line = 'xd1 xd2 Xd'
print(''.join(x.upper() + ' ' for x in line.split() if len(x) > 2))

#rozszerzona składnia yield
#czyli yield from

def fg(N):
    yield from range(N)
    yield from (x ** 2 for x in range(N))

#ta funkcja jest taka sama jak:

def fg_prim(N):
    for i in range(N): yield i
    for i in (x ** 2 for x in range(N)): yield i

#646 

#generatory jako argumenty funkcji 

def f(a,b,c) : print(a,b,c)
#gwiazdka rozpakowuje sekwencje
f(*(x ** 2 for x in range(3)))

#załadowanie generatora do lambdy

F = lambda x: (i**2 for i in range(x))
G = F(5)
print(next(G))
print(next(G))
print(next(G))
print(next(G))
print(next(G))
G = F(6)
print(next(G))
print(next(G))
print(next(G))
print(next(G))
print(next(G))
print(next(G))
print(list(G)) #pusta
G = F(5)
print(list(G)) #niepusta

def permute1(seq):
    if not seq:
        return [seq]
    else:
        res = []
        for i in range(len(seq)):
            rest = seq[i+1:] + seq[:i]  #biorę i-ty środkowy  zakres, ale wywalam 1 element
            for x in permute1(rest):
                res.append(seq[i:i+1] + x)
        return res

#to samo za pomocą generatora

def permute2(seq):
    if not seq:
        yield  seq
    else:
        for i in range(len(seq)):
            rest = seq[:i] + seq[i+1:]
            for x in permute2(rest):
                yield seq[i:i+1] + x

L = "ABFD"
print(permute1(L))

#własna implementacja funkcji map jako lista składana oraz wyrażenie generatora
def mymap(func,*seqs):
    return [func(*args) for args in zip(*seqs)]

def mymap2(func,*seqs):
    return (func(*args) for args in zip(*seqs)) #zwracam wyrażenie generatora ,więc nie muszę używać słowa yield

#własna implementacja funkcji zip

def myzip(*seqs):
    minlen = min(len(S) for S in seqs)
    return (tuple(S[i] for S in seqs) for i in range(minlen))

#wszystkie obiekty składane

L = [x * x for x in range(10)] # Lista składana: zwraca listę
G = (x * x for x in range(10)) # Wyrażenie generatora: zwraca elementy na żądanie
S = {x * x for x in range(10)} # Zbiór składany, dostępny w wersjach 3.x i 2.7
D = {x: x * x for x in range(10)} # Słownik składany, dostępny w wersjach

#w zbiorach i słownikach składanych również można używać filtrów if 

{x * x for x in range(10) if x % 2 == 0}
{x: x * x for x in range(10) if x % 2 == 0}
#pamiętaj ,że zbiory i słowniki nie zachowują kolejności oraz duplikatów kluczy!

