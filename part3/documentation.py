import sys

# takich komentarzy należy używać jedynie do opisywania konkretnych kawałeczków
#kodu , nie powinny być długie

# nazwy zaczynające się od __ są związane z interpreterem
# nazwy zaczynajace się od _ są prytwanymi nieformalnymi nazwami 


L = [line for line in dir(sys) if not line.startswith('__')]
for line in L:
    print(line) 

print(dir([])) # wyświetlenie wszystkich artrybutów list

def dir1(x):
    return [line for line in dir(x) if not line.startswith('__')]

def dir2(x):
    for line in dir1(x):
        print(line)

dir2(dict) # dict jest instancją konstruktora

#dokumentować można i tak
def sqrT(x):
    """
    Pewna dokumentacja \n
    xd
    """
    return x ** 3

print(sqrT.__doc__) # wyświetla dokumentację zawartą w komentarzach
print(sys.__doc__)
print(sys.base_prefix.__doc__)
# tak samo to działa w klasach

#bardziej użyteczne ,czyli help
help(sys.exit)
help(sys)

#polecenie help można zastosować do istniejących obiektów oraz ich typów

#by wygenerować plik dokumentacyjny należy wydać poniższe polecenie w powłoce
#python -m pydoc -b

#513 zrób quiz