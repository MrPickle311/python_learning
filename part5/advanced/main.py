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