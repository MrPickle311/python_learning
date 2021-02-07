#generatory generują sekwencję wyników stopniowo, nie w jednej całości.
#nie zwracają wyniku ,tylko generator wyników
#potrafią zawieszać swoje działanie i wznawiać je sekwencyjnie
#w miarę generowania kolejnych wartości
#są swoimi własnymi iteratorami jak pliki
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

