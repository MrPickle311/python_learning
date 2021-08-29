def raise1():  raise IndexError
def noraise(): return
def raise2():  raise SyntaxError

for func in (raise1, noraise, raise2):
    print('<%s>' % func.__name__)
    try:
        try:
            func()
        except IndexError:
            print('caught IndexError')
    finally:
        print('finally run')
    print('...')

# Słowo break pozwala na wyjście z najbliższej pętli
# Jednak stosując wyjątki można wyjść z dowolnie zagnieżdżonej pętli

class Exitloop(Exception): pass

try:
    while True:
        while True:
            for i in range(10):
                if i > 3: raise Exitloop # Instrukcja break spowodowałaby wyjście
                print('pętla 3: %s' % i) # tylko jeden poziom wyżej
        print('pętla 2')
    print('pętla 1')
except Exitloop:
    print('kontynuacja')

# Wyjątki nie są błędami , można je użyć do odpalania flag

class Found(Exception): pass

def searcher():
    if ...sukces...:
        raise Found()
    else:
        return

try:
    searcher()
except Found:
    ...sukces...
else:
    ...porażka...

# Więcej informacji na temat funkcji sys.exc_info
# wywołanie to zwraca krotkę 3 elementową z następującymi informacjami

# typ to klasa obsługiwanego wyjątku,
# wartość to instancja klasy wyjątku, która została zgłoszona,
# ślad to obiekt śladu reprezentujący stos wywołań w momencie, w którym początkowo
# wystąpił wyjątek, a moduł traceback wygenerował komunikat o błędzie.

import traceback

def inverse(x):
    return 1 / x

try:
    inverse(0)
except Exception:
    traceback.print_exc(file=open('badly.exc', 'w'))
print('Bye')

# Powyższy kod zapisuje w pliku komunikat o błędzie do pliku

# NIE PRZECHWYTUJ ZBYT MAŁO ORAZ ZBYT DUŻO
# UŻYWAJ HIERARCHII WYJĄTKÓW

