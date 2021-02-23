import sys
sys.path.append('C:/Users/Damian/AppData/Local/Programs/Python/Python39/Lib/site-packages')

#trochę się pobawiłem prostą biblioteką graficzną

#
#from graphics import *
#win = GraphWin(width = 200, height = 200) # create a window
#win.setCoords(0, 0, 10, 10) # set the coordinates of the window; bottom left is (0, 0) and top right is (10, 10)
#mySquare = Rectangle(Point(1, 1), Point(9, 9)) # create a rectangle from (1, 1) to (9, 9)
#mySquare.setFill(color='red')
#line = Line(Point(1, 1), Point(9, 9))
#line.setFill(color='blue')
#line.setWidth(4)
#mySquare.draw(win) # draw it to the window
#line.draw(win)
#win.getMouse() # pause before closing

# Importowanie z użyciem kropek wiodących:
# można użyć wiodącej
# kropki w instrukcjach from, aby wymusić import względny w ramach pakietu: tego
# typu importy wyszukują moduły tylko w katalogu bieżącego pakietu i nie znajdą modułów
# o tych samych nazwach zapisanych w innych miejscach ścieżki wyszukiwania (sys.path).
# W efekcie moduły danego pakietu mogą przeciążać moduły zewnętrzne.

# Importowanie bez użycia kropek wiodących
# importy w ramach pakietu są domyślnie bezwzględne — jeżeli nie zastosowano wiodącej
# kropki, import pomija moduły pakietu i wyszukuje wyłącznie w ścieżce sys.path.


# from . import math

# Jej wykonanie spowoduje zaimportowanie modułu o nazwie math, położonego w tym samym
# katalogu pakietu, co moduł, w którym występuje ta instrukcja

# from __future__ import absolute_import

# Po włączeniu tej opcji import bez wiodącej kropki w nazwie
# modułu zawsze powoduje, że Python pomija względne komponenty ścieżki wyszukiwania
# importu modułu i zamiast tego szuka wyłącznie w katalogach zawartych w sys.path

# W Pythonie 3.x instrukcja import nazwa_modułu
# zawsze działa w trybie bezwzględnym, czyli pomija bieżący katalog pakietu

# from .string import name1, name2 # Importuje nazwy z mypkg.string
# from . import string # Importuje mypkg.string
# from .. import string # Importuje string z tego samego poziomu, na którym znajduje się mypkg

# Załóżmy ,że mamy następujący układ plików

#mypkg\
#   __init__.py
#   main.py
#   string.py

#tak więc

import string 
from string import name
# zaimportuje plik string.py spoza tego pakietu 

from . import string
from .string import name1, name2
#zaimportuje string.py z pakietu tzw. import względny

from . import string # Składnia importów względnych

# Podwójna kropka spowoduje
# względny import, rozpoczynając od katalogu nadrzędnego, na przykład:

from .. import spam # Importuje spam sąsiadujący z mypkg

# Reguły importowania
# 
# 1.Importy względne są stosowanie wyłącznie wewnątrz pakietów 
# 2. Względne importy stosuje się wyłącznie w instrukcji from

# Różnice w wersjach

# Importowanie z kropką: from . import m, from .m import x
# Jest względne zarówno w wersji 2.x, jak i 3.x.

# Importowanie bez kropki: import m, from m import x
# Jest najpierw względne, a następnie bezwzględne w wersji 2.x, a bezwzględne tylko w wersji 3.x.

# normalnych importów używaj do szukania w bibliotekach
# względnych do odnajdywania się między pakietami

# 762 
# Pułapki związane z importem względnym w pakietach:

# Pakiety , a programy

# Korzystanie z importu względnego uniemożliwia tworzenie pakietów, które służą zarówno
# jako programy wykonywalne, jak i pakiety do importu z zewnątrz.
# niektóre pliki również nie mogą już służyć jednocześnie jako moduły skryptów i moduły pakietów

# więc jest możliwość zajścia potrzeby ,by pliki-moduły programu wydzielić do osobnego podkatalogu , oddzielonego
# od plików skryptów najwyższego poziomu

#więc import z pełnymi ścieżkami pakietu

from system.section.mypkg import mod # Działa zarówno w trybie program, jak i pakiet

# trybie pakietu zwykłe importowanie nie ładuje modułów
# znajdujących się w tym samym katalogu, chyba że katalog ten jest głównym katalogiem pakietu

# Jeśli mamy mieszane zastosowanie ,to można używać katalogu nadrzędnego jako samodzielnego programu 
# ,a katalog zagnieżdżony nadal może służyć jako pakiet do użytku dla innych programów

# code\pkg\main.py
import sub.spam # <== Działa, jeżeli przeniesiemy moduły do podkatalogu „poniżej” pliku głównego
# code\pkg\sub\spam.py
from . import eggs # Importy względne wewnątrz pakietu teraz działają poprawnie (moduły w podkatalogach)
# code\pkg\sub\eggs.py
print('Eggs' * 4)

# to rozwiązanie będzie działać we wszystkich wersjach
# ale nie można tutaj indywidualnie testować modułów

# c:\code> py 3 pkg\sub\spam.py # Poszczególne moduły nie mogą być uruchamiane indywidualnie, np. do testów
# SystemError: ... cannot perform relative import

# by to załatać można użyć importu bezwzględnego z użyciem pełnej ścieżki

# code\pkg\main.py
import spam
# code\pkg\spam.py
import pkg.eggs # <== Pełne ścieżki działają we wszystkich przypadkach; 2.x+3.x
# code\pkg\eggs.py
print('Eggs' * 4)

# przykład jak powinno się to prawidłowo robić trochę inną metodą:

# code\dualpkg\m1.py
def somefunc():
print('m1.somefunc')
# code\dualpkg\m2.py
import dualpkg.m1 as m1 # Zamień ten wiersz na odpowiednie polecenie importu
def somefunc():
m1.somefunc()
print('m2.somefunc')
if __name__ == '__main__':
somefunc() # Autotest lub kod skryptu najwyższego poziomu


# Pakiety przestrzeni w Python 3.3 

# pozwala pakietom
# składać się z wielu katalogów i nie wymaga pliku inicjującego __init__.py

# Python 3.3 posiadają tylko dwa warianty pakietów
# 1.Oryginalny model, obecnie znany jako pakiety regularne lub po prostu zwykłe
# 2.Pakiety przestrzeni nazw

#Algorytm w wersji 3.3

# 1. Jeżeli zostanie znaleziony plik nazwa_katalogu\spam\__init__.py, importowany i zwracany jest
# zwykły pakiet.
# 2. Jeżeli zostanie znaleziony plik nazwa_katalogu\spam.py (lub spam.pyc lub inne rozszerzenie
# modułu), importowany i zwracany jest zwykły pakiet.
# 3. Jeżeli zostanie znaleziony katalog nazwa_katalogu\spam, zostanie on zapisany, a skanowanie
# będzie kontynuowane w następnym katalogu ze ścieżki wyszukiwania.
# 4. Jeżeli żaden z powyższych plików lub katalogów nie zostanie znaleziony, skanowanie
# będzie kontynuowane od następnego katalogu ze ścieżki wyszukiwania.

# w kroku 3 jest tworzony pakiet przestrzeni nazw 
# reszta jest w folderze namespace packages

