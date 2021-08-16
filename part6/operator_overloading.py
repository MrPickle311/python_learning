
class Number:
    def __init__(self, start):
        self.data = start
    def __sub__(self, other):
        return Number(self.data - other)

# Podczas tworzenia instancji najpierw jest wywoływana metoda __new__, która tworzy
# i zwraca obiekt instancji. Obiekt ten jest następnie przekazywany metodzie __init__
# do zainicjowania. Ponieważ metoda __new__ posiada wbudowaną implementację
# i redefiniuje się ją tylko na potrzeby bardzo specyficznych zastosowań,

# Tutaj są opisane wszystkie możliwe operatory do przeciążenia
# https://docs.python.org/3/reference/datamodel.html

# Indeksowanie i wycinanie — __getitem__ i __setitem__

# Przeciążanie operatora indeksowania 

class Indexer:
    def __getitem__(self, index):
        return index ** 2

X = Indexer()
print (X[2])

for i in range(5):
    print(X[i], end=' ')

# Dzięki niej można ogarniać również wycinki

# Jak działają wycinki od kuchni ?

L = [5, 6, 7, 8, 9]
print(L[2:4])
print(L[1:])
print(L[:-1])
print(L[::2])

# W rzeczywistości parametry wycinania są pakowane w specjalny obiekt wycinka, który jest
# przekazywany do instancji listy.

print(L[slice(2, 4)])
print(L[slice(1, None)])
print(L[slice(None, 1)])
print(L[slice(None, None, 2)])

# Nasz poprzedni przykład nie obsłuży wycinania, po-
# nieważ metoda __getitem__ zakłada, że otrzymała liczbę całkowitą, co naprawiamy w po-
# niższym przykładzie.

class Indexer2:
    data = [5, 6, 7, 8, 9]
    def __getitem__(self, index):
        print('getitem:', index)
        return self.data[index]

X = Indexer2()

print(X[0])
print(X[1])
print(X[-1])

# W razie potrzeby metoda __getitem__ może sprawdzać typ argumentu i wyodrębniać granice
# obiektu wycinka. Taki obiekt posiada atrybuty start , stop i step . Każdy z nich, jeżeli zostanie
# pominięty, przyjmuje wartość None.

class Indexer3:
    def __getitem__(self, index):
        # Sprawdzenie trybu użycia
        if isinstance(index, int): print('indeks', index) 
        else: print('wycinek', index.start, index.stop, index.step)
    def __setitem__(self, index, value):
        self.data[index] = value

# Przechwytuje przypisania do indeksu lub wycinka
# Przypisanie do indeksu lub wycinka

X = Indexer3()
print(X[99])
print(X[1:99:2])
print(X[1:])

# Metoda __setitem__ (Parz na klasę wyżej) implementuje analogiczny mechanizm przypisywania wartości zarówno
# dla indeksów, jak i dla wycinków


# Metoda __index__ służy bowiem do przekształcania obiektu na liczbę całkowitą i jest wyko-
# rzystywana przez funkcje przekształcające obiekty na ciągi liczb.

class C:
    def __index__(self):
        return 255

X = C()
print(hex(X))

# Jeżeli nie jest konkretnie zdefiniowana żadna z metod :  __iter__ lub __next__, 
# instrukcja for przy każdej iteracji odczytuje jeden element, wyko-
# rzystując kolejny indeks, licząc od zera, aż zostanie wywołany wyjątek IndexError końca zakresu.

class StepperIndex:
    def __getitem__(self, i):
        return self.data[i]

X = StepperIndex()
X.data = "Mielonka" # X jest instancją klasy StepperIndex
print(X[1]) # Indeksowanie wywołuje __getitem__
for item in X:
    print(item, end=' ')

# Konteksty iteracyjne działają przez wywoływanie wbudowanej funkcji iter , wywołującej
# metodę __iter__ obiektu iterowanego, która z kolei powinna zwracać iterator. Jeśli tak się
# stanie, Python w kolejnych iteracjach wywołuje metodę __next__ iteratora zwracającą kolejne
# elementy, aż zostanie wywołany wyjątek StopIteration .

# Iteratory zdefiniowane przez użytkownika

class Squares:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop
    def __iter__(self):
        return self
    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2

for i in Squares(1, 5): # for wywołuje metodę iter(), która wywołuje __iter__()
    print(i, end='')    # Każda iteracja wywołuje metodę next()

X = Squares(1, 5)
I = iter(X) # iter wywołuje __iter__
next(I) # next wywołuje __next__
next(I)

# Czyli wychodzi na to ,że muszą być oba operatory zdefiniowane
print('')

# Na przykład aktualna metoda __iter__ klasy Squares zawsze zwraca atrybut self zawie-
# rający tylko jedną kopię stanu iteracji i dlatego wykonywana jest pojedyncza iteracja. Instan-
# cja klasy po zakończonej iteracji jest pusta. Ponownie wywołana metoda __iter__ tej samej
# instancji znów zwraca atrybut self zawierający stan instancji, w jakim została pozostawiona. Dla
# każdej nowej iteracji zawsze trzeba tworzyć nowy iterowalny obiekt instancji.

X = Squares(1, 5)     # Utworzenie obiektu iteratora ze stanem
print([n for n in X]) # Wyczerpuje elementy: metoda __iter__ zwraca self
print([n for n in X])  # Teraz jest pusta: metoda __iter__ zwraca self

[n for n in Squares(1, 5)] # Utworzenie nowego obiektu iteratora
print(list(Squares(1, 3))) # Nowy obiekt dla każdego nowego wywołania __iter__
 
# Wiele iteracji po jednym obiekcie

#Jeśli samodzielnie definiujemy własne iteratory w postaci klas, możemy zdecydować, czy
# chcemy obsługiwać pojedynczą iterację, czy wielokrotną.

class SkipObject:
    def __init__(self, wrapped): # Zapisanie elementu, który ma być użyty
        self.wrapped = wrapped
    def __iter__(self):
        return SkipIterator(self.wrapped) # Za każdym razem nowy iterator


class SkipIterator:
    def __init__(self, wrapped): 
        self.wrapped = wrapped # Informacje o stanie iteratora
        self.offset = 0
    def __next__(self):
        if self.offset >= len(self.wrapped): # Zakończenie iteracji
            raise StopIteration
        else:
            item = self.wrapped[self.offset] # Inaczej zwrócenie elementu i pominięcie
            self.offset += 2
            return item

# By uzyskać ten sam efekt za pomocą
# iteratorów zdefiniowanych przez użytkownika, __iter__ musi po prostu zdefiniować nowy
# obiekt stanu dla iteratora, zamiast zwracać self .

print('\n')

alpha = 'abcdef'
skipper = SkipObject(alpha) # Utworzenie obiektu pojemnika
I = iter(skipper) # Utworzenie na nim iteratora
print(next(I), next(I), next(I)) # Odwiedzenie wartości przesunięcia 0, 2, 4

for x in skipper: # for automatycznie wywołuje __iter__
    for y in skipper: # Zagnieżdżone for za każdym razem wywołują __iter__
        print(x + y), # Każdy iterator ma własny stan i przesunięcie

# Alternatywa: metoda__iter__ i instrukcja yield

class Squares: # Metoda __iter__ + instrukcja yield
    def __init__(self, start, stop): # Automatyczna/domniemana metoda __next__
        self.start = start
        self.stop = stop
    def __iter__(self):
        for value in range(self.start, self.stop + 1):
            yield value ** 2

S = Squares(1, 5) # Uruchomienie __init__: klasa zapisuje stan instancji
print(S)

I = iter(S) # Uruchomienie __iter__: zwrócenie generatora
print(I)
print(next(I)) # Uruchomienie metody __next__ generatora

# Zakodowanie generatora w postaci metody __iter__ skutkuje usunięciem z kodu pośredniego elementu
# jednak w obu przypadkach tworzony jest nowy obiekt generatora dla każdej iteracji:

# Jeżeli metoda __iter__ istnieje, jest wywoływana podczas iteracji i zwraca nowy gene-
# rator zawierający metodę __next__ .
# Jeżeli metoda __iter__ nie istnieje, kod tworzy generator, który zwraca samego siebie
# dla metody __iter__ .

# Ta metoda automatycznie obsługuje wielokrotne, aktywne iteratory

S = Squares(1, 5)
I = iter(S)
print(next(I), next(I))
J = iter(S)
print(next(J))

# To samo można osiągnąć bez generatorów ,ale kod będzie dłuższy

class Squares:
    def __init__(self, start, stop):
        # Generator bez instrukcji yield
        self.start = start
        # Wielokrotne skanowanie: dodatkowy obiekt
        self.stop = stop
    def __iter__(self):
        return SquaresIter(self.start, self.stop)

class SquaresIter:
    def __init__(self, start, stop):
        self.value = start - 1
        self.stop = stop
    def __next__(self):
        if self.value == self.stop:
            raise StopIteration
        self.value += 1
        return self.value ** 2

# Kod klasy SkipObject przy wykorzystaniu generatorów

class SkipObject:
    # Kolejny generator oparty na __iter__ + yield
    def __init__(self, wrapped):
        # Zakres instancji zachowywany normalnie
        self.wrapped = wrapped
        # Lokalny stan zapisywany automatycznie
    def __iter__(self):
        offset = 0
        while offset < len(self.wrapped):
            item = self.wrapped[offset]
            offset += 2
            yield item

skipper = SkipObject('abcdef')
I = iter(skipper)
print(next(I),next(I),next(I))
for x in skipper: # Za każdym razem wywoływana jest metoda __iter__: nowy generator
    for y in skipper:
        print(x + y, end=' ')

print('')

# W przypadku iteratorów klasy implementują operator przynależności in i wykorzystują
# metodę __iter__ albo __getitem__ . W celu zastosowania bardziej zaawansowanej logiki
# klasy mogą również implementować metodę __contains__ : gdy ta metoda jest dostępna, jest
# preferowana i ma przewagę nad __iter__ , która z kolei ma pierwszeństwo przed
# __getitem__ .

class Iters:
    def __init__(self, value):
        self.data = value
    def __getitem__(self, i): # Metoda zastępcza do użycia przez iterację
        print('get[%s]:' % i, end='') # oraz do indeksowania i wycinania
        return self.data[i]
    def __iter__(self): # Metoda preferowana w iteracji 
        print('iter=> ', end='') # Pozwala na użycie tylko jednego iteratora
        self.ix = 0
        return self
    def __next__(self):
        print('next:', end='')
        if self.ix == len(self.data): raise StopIteration
        item = self.data[self.ix]
        self.ix += 1
        return item
    def __contains__(self, x): # Metoda preferowana w operacji 'in'
        print('contains: ', end='')
        return x in self.data
    next = __next__  # Kompatybilność z wersją 2.x/3.x

X = Iters([1, 2, 3, 4, 5])
print(3 in X)

for i in X:
    print(i, end=' | ')

print()
print([i ** 2 for i in X])  # Inne konteksty iteracyjne
print(list(map(bin, X)))


I = iter(X)
while True: # Ręczna iteracja (demonstracja mechanizmu stosowanego w kontekstach iteracyjnych)
    try:
        print(next(I), end=' @ ')
    except StopIteration:
        break

# Gdy nie będzie metody __contains__ to zostanie wywołana metoda __iter__
# A gdy nie będziemy mieć ich obu ,to zostanie wywołana metoda __getitem__

# To samo ,ale na generatorach
class Iters2:
    def __init__(self, value):
        self.data = value
    def __getitem__(self, i):
        print('get[%s]:' % i, end='')
        return self.data[i]
    def __iter__(self):
        print('iter=> next:', end='')
        for x in self.data:
            yield x
        print('next:', end='')
    def __contains__(self, x):
        print('contains: ', end='')
        return x in self.data

# Czyli te dodatkowe operatory po prostu specjalizują nam konkretne operacje
# a __getitem__ zbiera resztę tego , czego my nie obsłużyliśmy

# Dostęp do atrybutów — __getattr__ oraz __setattr_

# Metoda __getattr__ przechwytuje odwołania do atrybutów. Jest wywoływana z nazwą atrybutu
# jako łańcuchem znaków, zawsze gdy próbujemy zapisać w składni kwalifikującej instancję
# z niezdefiniowaną (nieistniejącą) nazwą atrybutu. Nie jest wywoływana, kiedy Python może odna-
# leźć atrybut, wykorzystując do tego procedurę wyszukiwania w drzewie dziedziczenia.

print('\n')

class Empty:
    def __getattr__(self, attrname):
        if attrname == "age":
            return 40
        else:
            raise AttributeError(attrname)
    def __setattr__(self, attr, value):
        if attr == 'pay':
            self.__dict__[attr] = value + 10 # Niedozwolone self.name=val ani zewnętrzna funkcja setattr()
        else:
            raise AttributeError(attr + ' nie jest dozwolony')

X = Empty()
print(X.age)

# Metoda __setattr__ jest nieco trudniejsza w użyciu, ponieważ przypisanie do dowolnych atrybutów self
# wewnątrz wywołania metody __setattr__ ponownie wywołuje __setattr__ , powodując
# nieskończoną pętlę rekurencji
# Należy zapobiec powstaniu pętli poprzez zakodowanie
# przypisania atrybutu instancji w postaci przypisania klucza słownika. Oznacza to, że trzeba
# użyć zapisu self.__dict__['name'] = x zamiast self.name = x .

X.pay = 100
print(X.pay)

# Argumentem trzeciej metody do zarządzania atrybutami, __delattr__ , jest ciąg znaków zawie-
# rający nazwę atrybutu. Tak samo trzeba postępować jak wyżej (słownik)

# Emulowanie prywatności w atrybutach instancji

class PrivateExc(Exception): pass

class Privacy:
    def __setattr__(self, attrname, value):
        if attrname in self.privates:
            raise PrivateExc(attrname, self)
        else:
            self.__dict__[attrname] = value

class Test1(Privacy):
    privates = ['age']

class Test2(Privacy):
    privates = ['name', 'pay']
    def __init__(self):
        self.__dict__['name'] = 'Amadeusz'

# Ale to rozwiązanie jest złe , lepsze jest w Dekoratorach

# 945 Dodawanie prawostronne i miejscowa modyfikacja:

# Każdy operator binarny ma wariant lewy, prawy
# i miejscowy. Nawet jeżeli nie zakoduje się wszystkich trzech i stosowany jest wariant domyślny

class Commuter:
# Przeniesienie klasy operandu na wynik
    def __init__(self, val):
        self.val = val
    def __add__(self, other):
        if isinstance(other, Commuter): # Sprawdzenie typu w celu uniknięcia zagnieżdżenia obiektów
            other = other.val
        return Commuter(self.val + other) # Else i wynik drugiej instancji Commuter
    def __radd__(self, other):
        return Commuter(other + self.val)
    def __str__(self):
        return '<Commuter: %s>' % self.val

x = Commuter(88)
y = Commuter(99)
print(x + 1) # __add__: instancja + nieinstancja
print(1 + y) # __radd__: nieinstancja + instancja
print(x + y) # __add__: instancja + instancja, wywołuje __radd__

# Inne możliwe implementacje __radd__

class Commuter2:
    def __init__(self, val):
        self.val = val
    def __add__(self, other):
        return self.val + other
    def __radd__(self, other):
        return self.__add__(other) # Jawne wywołanie __add__

class Commuter4:
    def __init__(self, val):
        self.val = val
    def __add__(self, other):
        return self.val + other
    __radd__ = __add__ # Alias: usunięcie pośrednika

# Dodawanie w miejscu +=

class Number:
    def __init__(self, val):
        self.val = val
    def __iadd__(self, other):# __iadd__ wywołuje: x += y
        self.val += other # Z reguły zwraca self
        return self

x = Number(5)
x += 1
x += 1
print(x.val)

# Wywołania — __call__949

class Callee:
    def __call__(self, *pargs, **kargs):# Przechwytuje wywołania instancji
        print('Wywołanie:', pargs, kargs)# Akceptuje dowolne argumenty
C = Callee()
C(1, 2, 3)
C(1, 2, 3, x=4, y=5)

# Porównania — __lt__, __gt__ i inne

class C:
    data = 'spam'
    def __gt__(self, other):
        return self.data > other
    def __lt__(self, other):
        return self.data < other

X = C()
print(X > 'ham') # True (wywołuje __gt__)
print(X < 'ham') # False (wywołuje __lt__)

# awda zwrócona przez
# operator == nie oznacza, że operator != na tych samych operandach zwróci fałsz, dlatego
# metody __eq__ i __ne__ powinny być zdefiniowane w sposób niezależny

# Testy logiczne — __bool__ i __len__

class Truth:
    def __bool__(self): return True
    def __len__(self): return 0

X = Truth()
if X: print('tak!')

# Python najpierw próbuje bezpo-
# średnio uzyskać wartość logiczną, wywołując metodę __bool__ . Jeżeli tej metody nie ma, wy-
# wołuje metodę __len__ i określa wynik logiczny na podstawie długości obiektu.

# Destrukcja obiektu — __del__

class Life:
    def __init__(self, name='nieznajomy'):
        print('Witaj', name)
        self.name = name
    def __del__(self):
        print('Żegnaj', self.name)

# ale lepiej ich  nie uzywać , bo sprawiają kłopoty

# 961 Projektowanie z użyciem klas