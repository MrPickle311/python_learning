import sys
from imp import reload
#import bezwzględny
sys.path.append('c:/Users/Damian/Desktop/python_projects/python_learning/part5/module packages/namespace packages/ns')
import dir1.sub.mod1
# dodaję ns ,więc jego w nazwie importu już nie muszę uwzględniać ,bo jest on rootem

# przykład importu względnego jest w mod1.py

#Zagnieżdżanie pakietów przestrzeni nazw 

import dir2.sub.lower.mod3 as xd

print(xd.x)

# po prostu nie mieszaj nowego sposobu importowania ze starym

# W rezultacie zarówno pliki modułów, jak i zwykłe pakiety w dowolnym miejscu ścieżki wyszukiwania
# modułów mają pierwszeństwo przed katalogami pakietów przestrzeni nazw.

# Przydatne podsumowanie :

# Jaki jest cel umieszczania pliku __init__.py w katalogu pakietu modułu?

# Plik __init__.py służy do deklarowania i inicjalizacji zwykłego pakietu modułu. Python
# automatycznie wykonuje jego kod za pierwszym razem, gdy w procesie importujemy
# moduł za pośrednictwem katalogu. Przypisane zmienne pliku stają się atrybutami
# obiektu modułu utworzonego w pamięci i odpowiadającego temu katalogowi. Nie jest on
# opcjonalny — nie możemy importować modułów za pomocą składni pakietów, jeżeli
# katalog nie zawiera tego pliku.

# W jaki sposób możemy uniknąć powtarzania pełnej ścieżki pakietu za każdym razem,
# gdy odnosimy się do zawartości pakietu?

#Aby bezpośrednio skopiować zmienne z pakietu, należy użyć instrukcji from lub rozszerzenia
# as w połączeniu z instrukcją import, zastępując ścieżkę krótszym synonimem.
# W obu przypadkach ścieżka wymieniana jest tylko w jednym miejscu, czyli instrukcji from
# bądź import.

# Które katalogi wymagają, by znajdował się w nich plik __init__.py?

# W Pythonie 3.2 i wersjach wcześniejszych każdy katalog wymieniony w instrukcjach import
# oraz from musiał zawierać plik __init__.py. Pozostałe katalogi, w tym katalog zawierający
# pierwszy od lewej strony komponent ścieżki pakietu, nie muszą zawierać tego pliku.

# Kiedy w przypadku importowania pakietów musimy użyć instrukcji import zamiast from?

# W przypadku pakietów instrukcji import musimy użyć w miejsce from jedynie wtedy,
# gdy potrzebujemy uzyskać dostęp do tej samej zmiennej zdefiniowanej w więcej niż jednej
# ścieżce. Dzięki instrukcji import ścieżka sprawia, że referencje stają się unikalne, natomiast
# instrukcja from pozwala na wykorzystywanie tylko jednej wersji danej nazwy
# zmiennej (o ile do zmiany nazwy nie użyjesz rozszerzenia as).

# Jaka jest różnica między instrukcją from mypkg import spam a from . import spam?

# W Pythonie 3.x instrukcja from mypkg import spam definiuje import bezwzględny: pakiet
# mypkg jest wyszukiwany z pominięciem katalogu pakietu, w którym występuje ta instrukcja,
# to znaczy przeszukiwana jest wyłącznie ścieżka sys.path. Instrukcja from . import spam
# definiuje import względny: nazwa spam jest poszukiwana w odniesieniu do pakietu, w którym
# występuje ta instrukcja. W Pythonie 2.x import bezwzględny najpierw przeszukuje katalog
# pakietu, zanim przejdzie do ścieżki sys.path; import względny działa tak, jak to wcześniej
# opisywaliśmy.

# Czym jest pakiet przestrzeni nazw?

# Pakiet przestrzeni nazw jest rozszerzeniem modelu importu dostępnym w Pythonie 3.3
# i nowszych wersjach; reprezentuje pakiet składający się z jednego lub większej liczby katalogów,
# które nie zawierają plików __init__.py. Gdy Python znajdzie takie katalogi podczas
# wyszukiwania importu i nie znajdzie wcześniej prostego modułu lub zwykłego pakietu
# o takiej nazwie, tworzy pakiet przestrzeni nazw, który jest wirtualnym połączeniem
# wszystkich znalezionych katalogów o nazwie odpowiadającej nazwie żądanego modułu.
# Dalsze zagnieżdżone komponenty są wyszukiwane we wszystkich katalogach pakietu przestrzeni
# nazw. W rezultacie powstaje pakiet bardzo podobny do zwykłego pakietu, ale jego
# zawartość może być podzielona na wiele katalogów.