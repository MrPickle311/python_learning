# Przchwytywanie wyjątków

def fetcher(obj, index):
    a = obj[index]
    print('done') 
    return a

x = 'mielonka'

def catcher():
    try:
        fetcher(x, 8)
    except IndexError:
        print('mam wyjątek')
    print('kontynuuję') 

catcher()

# W Pythonie czyszczona jest cała pamięć wykorzystywana przez funk-
# cje, z których nastąpiło wyjście w wyniku wystąpienia wyjątku (w tym przykładzie fetcher ),
# i nie można wznowić ich wykonywania. Instrukcja try zarówno przechwytuje wyjątki, jak
# również określa, od którego miejsca wznawiane jest wykonywanie programu.

# Zgłaszanie wyjątków

# By ręcznie wywołać wyjątek, wystarczy wykonać instrukcję raise

try:
    raise IndexError
except IndexError:
    print('mam wyjątek')

# Wyjątki zdefiniowane przez użytkownika

class Bad(Exception): pass
def doomed():
    raise Bad()

try:
    doomed()
except Bad:
    print('przechwycenie Bad')

# Działania końcowe

# kombinacja try / finally określa działania końcowe,
# jakie zawsze zostaną wykonane przy wychodzeniu, bez względu na to, czy w bloku try wy-
# stąpi wyjątek.

try:
    fetcher(x, 3)
finally:
    print('po pobraniu')

def after():
    try:
        fetcher(x, 8)
    finally:
        print('po pobraniu')
    print('po try?')

after()

# Jeśli wywołanie funkcji zwróci wyjątek, nigdy nie
# wykonamy instrukcji print . Połączenie try / finally pozwala uniknąć tej pułapki — jeśli wyją-
# tek wystąpił w bloku try , bloki finally wykonywane są, kiedy program jest rozwijany.

