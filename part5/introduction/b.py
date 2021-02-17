import a #przypisanie modułu do zmiennej a 
#dopóki nie zaimportuję pliku a ,to nie mogę korzystać z nazw tam zdefiniowanych ,nawet jeśli
#ten i plik i a.py jest w tym samym folderze

#a = 'sd'to popsuje program
a.printSth('xd')

#importowanie odbywa się po uruchomieniu programu!
#kroki wykonywane podczas importowania
#1.odszukanie pliku modułu
#2.jeśli to konieczne ,to skompilowanie go do postaci kodu bajtowego
#3.wykonanie kodu modułu w celu utworzenia definiowanych przez niego obiektów

#1. Python ma jakąś swoją ścieżkę wyszukiwania,więc podawanie ścieżki do pliku modułu jest błędne składniowo
#2. Python podejmuje decyzję dot. tego ,czy skompilować kod do kodu bajtowego, pliki ,któe podlegają importowaniu są kompilowane przynajmniej raz 
#a ich kod bajtoway znajduje się w folderze __pycache__ , jeśli pliki nie były ostatnio aktualizowane to nie są ponownie kompilowane 
# ich rekompilacja odbywa się ,gdy pliki importowane zostały zaaktualizowane od czasu ostatniego uruchomienia programu   

#Python importuje jeden plik tylko jeden raz, czyli ładuje go do pamięci 
#skąd późniejsze importy w innych plikach nie wymagają już instrukcji import

