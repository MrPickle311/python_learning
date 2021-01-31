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

#Dopasowywanie argumentów 
#1-Pozycyjne
#2-Dopasowanie po nazwie argumentu
#3-Wartości domyślne
#4-Przekazywanie dowolnej liczby argumentów zgodnie z pozycją lub słowem kluczowym(zbieranie oraz rozpakowywanie) poprzez * lub **
#5-Argumenty , które MUSZĄ być przekazywane przez nazwę

#W wywołaniu funkcji argumenty muszą pojawiać się w następującej kolejności: dowolne argumenty
#pozycyjne (wartość), po których następuje kombinacja argumentów ze słowami
#kluczowymi (nazwa=wartość), obiekt iterowalny , a na końcu **słownik.
#W nagłówku funkcji argumenty muszą się pojawiać w następującej kolejności — normalne
#argumenty (wartość), po nich argumenty ze słowami kluczowymi (nazwa=wartość), potem
#forma *nazwa , następnie argumenty mogące być tylko słowami kluczowymi
#nazwa lub nazwa=wartość , a na końcu **nazwa.

#Python:
#1. Przypisuje argumenty niebędące słowami kluczowymi zgodnie z pozycją.
#2. Przypisuje argumenty będące słowami kluczowymi poprzez dopasowanie nazw.
#3. Przypisuje dodatkowe argumenty niebędące słowami kluczowymi do krotki *nazwa.
#4. Przypisuje dodatkowe argumenty będące słowami kluczowymi do słownika **nazwa.
#5. Przypisuje do argumentów nieprzypisanych wartości domyślne z nagłówka.

#definiowanie argumentów po słowie kluczowym
def f4(a,b,c):
    print(a,b,c)
f4(c=2,b=56,a=-1)

#wartości domyślne
def f5(x,y=5,z=3):
    print(x,y,z)
f5(78)
f5(z=6,y=0,x=7)
f5(x=7,z=6,y=0)
f5(7,z=6,y=0)
#f5(y=0,x=7,6) #tak nie można
f5(8,z=10)
f5(1,2,3)
f5(1,2)

#zbieranie niedopasowanych argumentów pozycyjnych w krotkę
def f6(a,b,*args):
    print(args)
f6(3,4,'23',2323,[2,3])

#zbieranie niedopasowanych argumentów po słowach kluczowych w słownik
def f7(**args):
    for key in args:
        print(key,args[key])
f7(xd=2,hello="helo",h=[2,3])

#połączenie kilku sposobów
def f8(a,b,*pargs,**kargs):
    print('Normal ',a,b)
    for (itr,pos) in enumerate(pargs):
        print('At pos : ' +str(itr) + ' is arg with: ' + str(pos))
    for (itr,key) in enumerate(kargs):
        print('At key : ' +str(itr) + ' is arg with: ' + str(kargs[key]))
f8(5,7,[2,3,4],'sdsds',2,name=2,surname='ok',lamba=['gromeka',5])

#teraz zrobię odwrotnie ,czyli rozpakuję argumenty w miejscu wywołania funkcji
def f9(a,b,c,d):
    print(a,b,c,d)
T = (3,'asda',[2,3,1])
T += ('sadsad',)
f9(*T)
#rozpakowanie krotki w miejscu wywołania

#rozpakowanie słownika w miejscu wywołania funkcji
D = dict(a='sds',b=5,c='abba',d=2)#nazwy kluczy w słowniku muszą być takie same jak nazwy
f9(**D)                           #argumentów funkcji
D = dict(k='sds',s=5,c='abba',d=2)
f8(5,6,*T,**D) # załadowanie tego do funkcji
f8(78,34,*(2,3,4,2,[23,23,23],'sdsd'),**{'name' : 'ok','sd':'xd'})
f8(78,34,*(2,3,4,2,[23,23,23],'sdsd'),hello=5,raw='raw',**{'name' : 'ok','sd':'xd'})#kombinacja ostateczna xd

#do funkcji można przekazać także inne funkcje
def f10(func,a,b,c):
    print('Im calling ' + func.__name__) #nazwa wartości argumentu
    func(a,b,c)
def funct(a,b,c):
    print(a,b,c)
f10(funct,1,2,3)

#tutaj argument c może być przekazany TYLKO przez słowo kluczowe
def f11(a,*b,c):
    print(a,*b,c)
f11(1,2,3,3,2,1,c=23)
f11(1,c=5)
f11(a=1,c=5)
f11(c=1,a=5)

#tutaj jest wymuszenie tego ,by b i c były przekazane jako słowa kluczowe
# * służy jako separator sposobu przekazywania arguentów
def f12(a,*,b,c='xd'):
    print(a,b,c)
f12(6,b=23,c=23)
f12(5,b=7)

#ten kod spadnie z rowerka
#def f13(a,b=5,*c,**q):
#    print(a,b,*c,**q)
#f13(5,42,4,3,k=1)

#takie same reguły są dla wywołań funkcji

#definicje funkcji min oraz max
def minmax(*args,sortMin=True):
    L = list(*args)
    L.sort()
    if sortMin == True:
        return L[0]
    else: return L[-1]
L = [2 ,1 -1,3]
print(minmax(L))
print(minmax(L,sortMin=False))

def intersect(*args):
    res = []
    for x in args:
        if x in res: continue
        for other in args[1:]:
            if x not in other:break
        else: res.append(x)
    return res
