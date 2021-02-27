from math import sqrt # teraz nie muszę odwoływać math.sqrt
from math import * # teraz wszystkie nazwy są kopiowane do zasięgu tego pliku
from math import * # może zaciemnić lokalne zmienne
from imp import reload # importowanie funkcji reload

import support
import support
from support import z # (1), tu odbywa się kopiowanie do lokalnego zasięgu 


#lub
k = support.z

#importowanie jest kosztowną operacja ,ale wiadomo ,że przeprowadza sie ją tylko raz
#bo potem leci z pamięci ,więc bezpośredni kod zewnętrznych modułów jest wykonywany TYLKO RAZ

#Pamiętaj! Niezależnie od tego w jaki sposób importujesz nazwy z modułu, to plik modułu i tak jest zawsze
#importowany w całości

# Jeśli taka sama nazwa jest zdefiniowana w dwóch modułach ,to używaj tylko import!
# Inaczej nastąpi nadpisanie
# Importowany plik nie widzi zmiennych w pliku , który go importuje
# za pomocą kropki '.' przemieszczamy się po kolejnych zagnieżdżeniach między modułami
# 

print(sqrt(4))
print(pow(2,3))

# import to instrukcja jak każda inna , nazwa z importu nie będzie dostępna dopóki interpreter do niej
# nie dojdzie

#UWAGA , w module support są dwie zmienne x - niemutowalne , y -mutowalne
y = [6,7,8] # modyfikacja y z modułu support
x = 1000 # modyfikacja lokalnego x
support.x = 999 # modyfikacja x z modułu

#ale jeśli nazwę niemutowalną zaimportuję bezpośrednio ( patrz (1) )
z = 500
#to ta wartość z modułu też się  NIE zmieni
print(support.z)

print(list(support.__dict__.keys())) # tak można wylistować wszystkie nazwy z modułu

#Przeładowywanie modułów

#funkcja reload pozwala na modyfikację części
#programu bez konieczności zatrzymywania całego programu

#ale modułów napisanych w C/C++ nie można przeładowowywać

# reload to funkcja , nie instrukcja 

# Ważne informacje o tej funkcji

# Za pomocą tej funkcji mogę zmienić plik .py w czasie działania programu np. dodać nową funkcję
# po czym mogę wczytać ten plik na nowo

# Ponoć dobre do GUI

# Funkcja reload wykonuje kod przeładowywanego modułu w bieżącej przestrzeni nazw tego modułu.
# Przypisania najwyższego poziomu w pliku zastępują nazwy nowymi wartościami.
# Przeładowanie ma wpływ na wszystkie klienty wykorzystujące instrukcję import do pobrania modułów.
# Przeładowanie ma wpływ jedynie na przyszłe wywołanie instrukcji from.

reload(support) # znów się wyświetli Some initialization...

from math import sqrt
reload(math)
# jeśli używam from do importowania ,to reload nie przeładuje prawidłowo modułu
# gdyż odbywa się kopiowanie

# tak to można załatać
from imp import reload
import math
reload(math)
from math import sqrt # Można też się poddać i użyć module.function()
sqrt(1, 2, 3)

# Nie importuj modułów siebie nazwajem

#Instrukcja from może zaciemnić znaczenie zmiennej (to, w którym module została zdefiniowana),
#może powodować problemy w czasie wywoływania funkcji reload (zmienna
#może odnosić się do poprzedniej wersji obiektów), a także może uszkadzać przestrzenie
#nazw (po cichu nadpisując zmienne wykorzystywane w zakresie bieżącym). Forma from *
#jest pod wieloma względami gorsza — może poważnie zniszczyć przestrzenie nazw i zaciemnić
#znaczenie zmiennych. Najlepiej jest używać jej oszczędnie.

# Tylko moduł wykonywany jako program widzi inne moduły wokół siebie w tym samym katalogu
# chyba ,że się da __init__.py lub można pokombinować z nowszymi pakietami