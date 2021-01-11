import builtins
#Zasady
#Moduł zawierający funkcję jest zasięgiem globalnym.
#Zasięg globalny rozciąga się jedynie na jeden plik.
#W Pythonie nie istnieje coś takiego jak jeden
#obejmujący wszystko globalny zasięg oparty na plikach
#Przypisane nazwy są lokalne, o ile nie zostaną zadeklarowane jako globalne lub nielokalne.
#Pamiętaj również o tym, że modyfikacje obiektów w miejscu nie klasyfikują zmiennych jako lokalnych
#Jeżeli na przykład
#nazwa L zostanie przypisana do listy na najwyższym poziomie modułu, instrukcja taka
#jak L.append(X) wewnątrz funkcji nie zaklasyfikuje L jako zmiennej lokalnej, natomiast L = X
#już tak.
#W tym pierwszym przypadku zmieniamy obiekt listy, do którego odwołuje się
#zmienna L, a nie samą zmienną L.

#w instrukcji def:
#przypisania nazw tworzą i modyfikują nazwy lokalne
#referencje do nazw przeszukują co najwyżej 4 zasięgi - 
#lokalny funkcji ,
# funkcji zawierających(może być więcej niż jedna, kilka )
#tę funkcję,globalny, wbudowany
#global - zasięg modułu, nonlocal - funkcja zawierająca

#LEGB - local,enclosing,global,built-in

#pętle for nie ograniczają zasięgu swoich zmiennych do zasiegu instrukcji
#w bloku try wszystko jest lokalne
#zasięg wbudowany zawiera się w module builtins ,jednak sam moduł trzeba zaimportować
#jednak można korzystać z niego bez jego importowania

#zasięg globalny
X = 2

#zasięg lokalny
def func():
    X = 3 # tworzenie zmiennej lokalnej
    print(X)
func()
print(X) # będzie 2 

print(dir(builtins))

#w następujacej funkcji funkcja open została przysłonięta przez zmienną open
def func2():
    open = 23
    # f = open("mydata.txt") nie zadziała
func2()

#NIE ZMIENIAJ DEFINICJI WBUDOWANYCH NAZW PYTHONA

#instrukcja global daje znać ,że funkcja zmieni jedną lub więcej nazw globalnych 

def func3():
    global X # te nazwy będą modyfikowane
    X = 20
func3()
print(X)

#prezentacja działania reguły legb
z,y = 2,3
def glob():
    global X
    X = z + y # zmienna globalna może się odnosić do innych globalnych bez global
glob()
print(X)

#541

#zasięgi zagnieżdżone
#Referencja -> szuka zmienną w zasiegu lokalnym funkcji ,a potem w zasiegach
#lokalnych wszystkich funkcji zawierających tę funkcję 
#potem global , a potem builtin

#Przypisanie tworzy lub modyfikuje zmienną w bieżącym zasięgu lokalnym
#nonlocal sprawia ,że przypisanie modyfikuje zmienną w zasięgu lokalnym najbliższej funkcji
#zawierającej

def f1():
    X = 99
    def f2():
        print(X) # można sięgnąć do X
    f2()
f1()

def f3():
    X = 88
    def f2():
        print(X)
    return f2
action = f3()#coś jak wskaźnik na funkcję
action() # wywołąnie f3.f2

#funkcje w Pythonie są obiektami jak wszystko inne
#nawet pamięta wartość zmiennej X
#takie funkcje (chodzi o tę zwróconą) będą zawsze pamiętać zmienne z otaczających je
#zasięgów 

#Funkcje fabrykujące (domknięcia)

def maker(N):
    def action(X):
        return X ** N
    return action
# tutaj wewnętrzna funkcja action pamięta argumenty N i dlatego każde wywołanie maker z innymi
# daje inny rezultat funkcji action

r1 = maker(3)
print(r1(2)) # pamięta 3
r2 = maker(5)
print(r2(2)) # pamięta 5
print(r2(3)) # pamięta 5

#lub użycie lambdy zamiast tego 
def maker2(N):
    return lambda X: X ** N
r3 = maker(2)
print(r3(3))

#549
#Funkcje fabrykujące kontra klasy, runda pierwsza