#argumenty niemutowalne są przekazywane przez wartość ,a mutowalne przez wskaźnik
#czyli wszystko idzie przez referencję
#działanie tego mechanizmu jest tożsame z zasadami dotyczącymi obiektów mutowalnych niemutowalnych
#przypomnij sobie ,jak to będzie wszystko rozmieszczone w pamięci?
def f1(a,b):
    a = 2
    b[0] = 'xd' # tutaj nastąpi zmodyfikowanie zewnętrznej listy
L = [1,2]
x = 1
f1(x,L)
print(L,x)

def f2(a):
    print(a)
#sposoby na to ,by funkcja nie modyfikowała zmiennych w funkcji
f2(L.copy())
f2(tuple(L))

#symulowanie zwracania kilku wartości przez funkcji
#za pomocą krotki
def f3():
    x = 5
    y = [1,2,3,'s']
    return x,y #zwraca krotkę
x,y = f3()
print(x,y)

#572
#Podstawy dopasowywania argumentów