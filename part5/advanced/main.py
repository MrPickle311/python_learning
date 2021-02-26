import sys
# reguły o których warto pamiętać
#1. Zawsze jestem w jakimś module
#2. Hermetyzuj wszystko i nie twórz zmiennych globalnych
#3. Niech wszystkie komponenty modułu mają to samo przeznaczenie 
#4. Minimalizuj liczbę połączeń między modułami
#5. Moduły nie powinny modyfikować zmiennych w innych modułach.

#moduł sub ma zmienne a i _b
#podłoga przed nazwą zmiennej sprawia ,że poprzez import w następującej postaci
from sub import *
# zmiena _b nie będzie widoczna
print(a)
#print(_b)

# alternatywnie można wykorzystać listę __all__ (nazwa sztywna) , która zawiera 
# wszystkie zmienne , które powinny mogą być udostępnione
# __all__ ma pierwszeństwo przed podłogami przed zmiennymi

print(_c)

#ale inne sposoby importowania pozwalają zaimportować wszystkie zmienne

# jeśli chcę skorzystać z przyszłych rozszerzeń ,to 
# from __future__ import nazwa_opcji
# musi się znaleźć na początku pliku

# Mieszane tryby użycia — __name__ oraz __main__ 781

# każdy moduł posiada wbudowany atrybut o nazwie __name__, który Python automatycznie
# tworzy i przypisuje w następujący sposób:

# 1.Jeżeli plik jest wykonywany jako plik programu najwyższego poziomu, po uruchomieniu
# atrybut __name__ ustawiany jest na ciąg znaków "__main__".
#2.Jeżeli plik jest importowany, atrybut __name__ jest zamiast tego ustawiany na nazwę modułu,
# którą znają jego klienty.

# W rezultacie moduł może testować swój własny atrybut __name__ w celu sprawdzenia, czy
# jest wykonywany, czy też importowany.

def tester():
    print("Jest Gwiazdka w niebie...")
if __name__ == '__main__': # Tylko przy wykonywaniu
    tester() # A nie przy importowaniu

# w zmiennej sys.argv są przechowywane argumenty wiersza poleceń

print(sys.argv)

# Po dokonaniu zmiany w liscie sys.path będzie ona miała wpływ na wszystkie przyszłe operacje importowania
# w Pythonie, ponieważ wszystkie operacje importowania i wszystkie pliki współdzielą
# jedną listę sys.path

# takie ustawienia ścieżki sys.path trwają jedynie na czas działania
# sesji Pythona lub programu (z technicznego punktu widzenia: procesu), który je utworzył. Nie są
# one zachowywane po zakończeniu działania Pythona

#moduły są obiektami więc mają swoje artrybuty
print(sys.__name__)
#print(sys.__dict__)
#print(sys.modules['sys'].__name__)

#importowanie moduuł jako ciągu znaków

import importlib
modname = 'string'
string = importlib.import_module(modname)
print(string)

# Przeładowywanie rekurencyjne
# Załóżmy ,że jakiś moduł A importuje moduły C i B
# Jeśli przeładuję funkcją reload() moduł A ,to nie zostaną przeładowane moduły C i B
# Zostaną tylko załadowane z pamięci i wykonane ponownie

# Funkcja reload_all() przeładowuje rekurencyjniew wszystkie moduły

import types
from imp import reload # from wymagane w wersji 3.x

def status(module):
    print('przeładowanie' + module.__name__)

def tryreload(module):
    try:
        reload(module) # 3.3 (tylko?) nie działa w przypadku niektórych
        # modułów
    except:
        print('Niepowodzenie: %s' % module)

def transitive_reload(module, visited):
    if not module in visited: # Przechwycenie cykli i powtarzających się modułów
        status(module) # Przeładowanie modułu
        tryreload(module) # Przejście do jego modułów podrzędnych
        visited[module] = True
        for attrobj in module.__dict__.values(): # Dla wszystkich atrybutów
            if type(attrobj) == types.ModuleType: # Rekurencja, jeśli to moduł
                transitive_reload(attrobj, visited)

def reload_all(*args):
    visited = {} # Główny punkt wejścia
    for arg in args: # Dla wszystkich przekazanych modułów
        if type(arg) == types.ModuleType:
            transitive_reload(arg, visited)

def tester(reloader, modname): # Kod autotestu
    import importlib, sys # Importowanie tylko podczas testu
    if len(sys.argv) > 1: modname = sys.argv[1] # wiersz polecenia (lub przekazany argument)
    module = importlib.import_module(modname) # Importowanie poprzez ciąg znaków reprezentujący
    # nazwę
    reloader(module) # Test przekazanego modułu

if __name__ == '__main__':
    tester(reload_all, 'string')

# 808

