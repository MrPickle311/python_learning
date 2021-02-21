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

# Podwójna kropka spowoduje
# względny import, rozpoczynając od katalogu nadrzędnego, na przykład:

from .. import spam # Importuje spam sąsiadujący z mypkg

#Względne importy a bezwzględne ścieżki pakietów 755
