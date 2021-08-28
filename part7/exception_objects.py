class General(Exception): pass
class Specific1(General): pass
class Specific2(General): pass

# Wszystkie klasy wyjątków muszą dziedziczyć po Exception
# Mogą być puste

def raiser0():
    X = General()          # Raise superclass instance
    raise X

def raiser1():
    X = Specific1()        # Raise subclass instance
    raise X

def raiser2():
    X = Specific2()        # Raise different subclass instance
    raise X

for func in (raiser0, raiser1, raiser2):
    try:
        func()
    except General:        # Match General or any subclass of it
        import sys
        print('caught: %s' % sys.exc_info()[0]) # uzyskanie dostępu do ostatnio zgłoszonego wyjątku

# Jeśli w instrukcji raise wymienimy nazwę klasy bez nawiasów,
# Python wywoła klasę bez argumentu konstruktora w celu utworzenia instancji za nas.

class E(Exception): pass

try:
    raise E('mielonka') # Można dodać informacje , które są przechwytywane przed nadrzędną klasę Exception
except E as X:
    print(X)
    print(X.args)
    print(repr(X))

# By zmienić sposób wyświetlania , to trzeba zdefiniować własną metodę __str__

# Wyjątki to normalne obiekty , więc można definiować każde inne ich elementy

class FormatError(Exception):
    def __init__(self, line, file):
        self.line = line
        self.file = file
    def logError(self):
        print('Błąd w', self.file, self.line)

def parser():
    raise FormatError(42, file='spam.txt')
try:
    parser()
except FormatError as X:
    X.logError()

