import a #przypisanie modułu do zmiennej a 
import sys
#dopóki nie zaimportuję pliku a ,to nie mogę korzystać z nazw tam zdefiniowanych ,nawet jeśli
#ten i plik i a.py jest w tym samym folderze

#a = 'sd'to popsuje program
a.printSth('xd')

#importowanie odbywa się po uruchomieniu programu!
#kroki wykonywane podczas importowania
#1.odszukanie pliku modułu
#2.jeśli to konieczne ,to skompilowanie go do postaci kodu bajtowego
#3.wykonanie kodu bajtowego modułu w celu utworzenia definiowanych przez niego obiektów

#1. Python ma jakąś swoją ścieżkę wyszukiwania,więc podawanie ścieżki do pliku modułu jest błędne składniowo

#2. Python podejmuje decyzję dot. tego ,czy skompilować kod do kodu bajtowego, pliki ,któe podlegają importowaniu są kompilowane przynajmniej raz 
#a ich kod bajtoway znajduje się w folderze __pycache__ , jeśli pliki nie były ostatnio aktualizowane to nie są ponownie kompilowane 
# ich rekompilacja odbywa się ,gdy pliki importowane zostały zaaktualizowane od czasu ostatniego uruchomienia programu   
# głowny plik z którego uruchamiamy apkę nie jest w ogóle kompilowany 
# pliki modułów są również rekompilowane przy zmianie wersji Pythona ,która widnieje na końcu pliku .pyc
# budowa nazwy pliku bajtowego : <nazwa_modułu>.<nazwa_implementacji>-<numer_wersji>.pyc

#3.Jeśli importowany plik modułu ma jakieś bezpośrednie instrukcje wykonawcze, to wykonają się ona podczas importowania tego modułu


#Python importuje jeden plik tylko jeden raz, czyli ładuje go do pamięci 
#skąd późniejsze importy w innych plikach nie wymagają już instrukcji import

#każdy moduł importowany
#jest domyślnie tylko raz na proces. Kolejne operacje importowania pomijają wszystkie trzy
#etapy i korzystają z modułu już załadowanego do pamięci.

#Python szuka plików modułów w następujących lokalizacjach:

#1.Katalog główny programu
#2.Katalogi PYTHNPATH (jeżeli są ustawione).
#3. Katalogi biblioteki standardowej.
#4. Zawartość wszystkich plików .pth (jeżeli są one obecne).
#5. Katalog site-packages dla zewnętrznych pakietów rozszerzeń.

#Zestawienie tych pięciu komponentów daje nam sys.path — mutowalną listę nazw katalogów,

#Kolejność przeszukiwania
#1.Ponieważ ten katalog zawsze przeszukiwany jest jako pierwszy, jeśli program jest w całości
#umieszczony w jednym katalogu, wszystkie operacje importowania będą działać automatycznie,
#bez konieczności konfigurowania ścieżki. Z drugiej strony, ponieważ katalog
#ten przeszukiwany jest jako pierwszy, jego pliki będą także przeciążały moduły o tej samej
#nazwie znajdujące się w katalogach podanych w innych miejscach ścieżki.
#2.Następnie Python przeszukuje wszystkie katalogi podane w zmiennej środowiskowej
#PYTHONPATH, od lewej do prawej strony (zakładając, że ją w ogóle ustawiliśmy; ta zmienna nie
#jest predefiniowana).
#W PYTHONPATH podaje się listę zdefiniowanych
#przez użytkownika i specyficznych dla platformy nazw katalogów zawierających pliki
#z kodem Pythona.
#3.Katalogi biblioteki standardowej (automatyczne)
#4.Pozwala użytkownikom
#dodawać katalogi do ścieżki wyszukiwania modułów przez proste umieszczenie ich po
#jednym w wierszu w pliku tekstowym kończącym się rozszerzeniem .pth
#W skrócie, pliki tekstowe z nazwami katalogów wstawione do odpowiedniego katalogu
#mogą pełnić tę samą rolę co zmienna środowiskowa PYTHONPATH.
#Na przykład, jeżeli korzystasz
#z systemu Windows i Pythona 3.3, ścieżkę wyszukiwania modułów możesz w prosty
#sposób rozszerzyć, umieszczając plik o nazwie myconfig.pth w głównym katalogu instalacyjnym
#Pythona (C:\Python33) lub w podkatalogu pakietów biblioteki standardowej
#(C:\Python33\Lib\sitepackages). W systemach uniksowych plik ten można umieścić na przykład
#w katalogu /usr/local/lib/python3.3/site-packages lub /usr/local/lib/site-python.
#Kiedy plik taki jest obecny, Python dodaje katalogi wymienione w wierszach pliku, od pierwszego
#do ostatniego, na końcu listy ścieżki wyszukiwania modułów
#5.Katalog Lib\site-packages dla zewnętrznych pakietów rozszerzeń (automatyczne)

for path in sys.path: #prwadziwa ścieżka wyszukiwania modułów
    print(path)

#Python automatycznie konfiguruje sys.path podczas startu programu

#modyfikując sys.path, możemy również modyfikować ścieżkę wyszukiwania dla wszystkich
#przyszłych importów. Takie zmiany trwają jednak tylko do końca czasu działania skryptu;
#zmienna PYTHONPATH i pliki .pth oferują bardziej trwałe sposoby modyfikowania tej ścieżki
#— pierwszy z nich dla użytkownika, a drugi dla instalacji.

#Jeżeli pliki b.py i b.so znajdują się w różnych katalogach, Python zawsze załaduje ten znaleziony
#w pierwszym (znajdującym się bardziej po lewej stronie) katalogu ścieżki wyszukiwania
#modułów w czasie przeszukiwania listy sys.path od lewej do prawej strony. Co się jednak
#dzieje, jeżeli Python znajdzie zarówno b.py, jak i b.so w tym samym katalogu? W takim przypadku
#Python postępuje zgodnie ze standardową kolejnością wybierania, choć nie ma żadnej
#gwarancji, że kolejność ta nie zmieni się w innych wersjach lub dystrybucjach. Nie powinieneś
#zatem polegać na tym, który rodzaj pliku o tej samej nazwie w danym katalogu
#wybierze Python — zamiast tego lepiej jest nadawać plikom różne nazwy lub skonfigurować
#ścieżkę wyszukiwania modułów w taki sposób, by nasze preferencje w zakresie wybierania
#modułów były bardziej oczywiste.
