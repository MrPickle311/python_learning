#pakietem jest folder zawierający kod Pythona

import sys
from imp import reload
sys.path.append('C:/Users/Damian/AppData/Local/Programs/Python/Python39/Lib/site-packages')
# tak można dodać zbiory pakietów 

import PySide6.QtGui
reload(PySide6.QtGui) #reload działa także z kropkami

# tutaj widzimy ,że z folderu/pakietu pyside6 importujemy plik QtGui 
# czyli przemieszczamy się wgłąb pakietów/folderów za pomocą kropek
# ale najbardziej nadrzędne foldery/pakiety ( tutaj pyside6 ) znajduje nam Python
# każdy katalog wymieniony

#######################################

# w ścieżce instrukcji importowania pakietu musi zawierać plik o nazwie __init__.py,
# w przeciwnym razie operacja importowania zakończy się niepowodzeniem.

# jeżeli struktura katalogów wygląda następująco:
# dir0\dir1\dir2\mod.py
# a instrukcja import ma następującą postać:
# import dir1.dir2.mod

# To zastosowanie mają poniższe reguły:
# 1.katalogi dir1 oraz dir2 muszą zawierać plik __init__.py,
# 2.katalog nadrzędny dir0 nie musi zawierać pliku __init__.py; jeżeli plik ten będzie się w nim
# znajdował, zostanie zignorowany,
# 3.katalog dir0, a nie dir0\dir1, musi być umieszczony w ścieżce wyszukiwania modułów
# czyli musi znajdować się w katalogu domowym użytkownika, katalogu bibliotek lub katalogu site-packages
# lub musi zostać umieszczony w zmiennej PYTHONPATH, pliku .pth albo ręcznie dodany do ścieżki sys.path

#W efekcie struktura katalogów tego przykładu powinna wyglądać następująco (wcięcia oznaczają
#zagnieżdżenia katalogów):
#dir0\ # Katalog w ścieżce wyszukiwania modułów
#   dir1\
#       __init__.py
#           dir2\
#               __init__.py
#               mod.py

# role tego pliku

# 1.Inicjalizacja pakietów
# Za pierwszym razem, gdy Python importuje coś za pomocą katalogu, automatycznie
# wykonuje cały kod z pliku __init__.py tego katalogu.
# Służą jako kod inicjalizujący pakietu 
# 2.Jednym z zadań plików __init__.py jest również zadeklarowanie, że dany katalog jest pakietem
# Pythona.
# 3.W modelu importowania pakietów ścieżki katalogów ze skryptu stają się po zaimportowaniu
# prawdziwymi ścieżkami zagnieżdżonych obiektów.
# 4. Zachowanie instrukcji from * . 
# W pliku __init__.py lista __all__ ma być listą nazw podmodułów, które powinny
# zostać zaimportowane, kiedy instrukcji from * użyjemy na nazwie pakietu
# Pliki __init__.py możemy również po prostu pozostawić puste, jeżeli ich rola wykracza poza nasze
# potrzeby (i szczerze mówiąc, w praktyce te pliki są najczęściej puste). Muszą jednak istnieć, aby
# importowanie katalogów w ogóle działało.

#####################################

# W przypadku pakietów lepiej jest używać instrukcji from zamiast samego import
# gdyż Python sam wyszukuje sobie ścieżkę do interesującego mnie pliku, jest to przydatne
# gdy zmieniam drzewo katalogów

# wszystkie zewnętrzne "ręcznie robione" czy tam z githuba biblioteki wsadzaj do jednego katalogu
# np. extern i stamtąd importuj ,by nazwy ich plików się nie pomieszały 

