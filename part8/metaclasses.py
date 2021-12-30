# te dwie poniższe instrukcje tak naprawdę robią to samo

class Test:
    pass


print(Test)

Test = type('Test', (), {})

print(Test)

# można też tak dodać w locie nowe zmienne

Test = type('Test', (), {'x': 5})
t = Test()

print(t.x)

# ale załóżmy, że jest sobie taka oto klasa


class Foo:
    def show(self):
        print('hi')


Test = type('Test', (Foo,), {'x': 5})
t = Test()
t.show()

# mozna tez dodawać normalne funkcje


def add_attribute(self):
    self.z = 11


Test = type('Test', (Foo,), {'x': 5, 'add_attribute': add_attribute})
t = Test()
t.add_attribute()
print(t.z)

# definicja prostej metaklasy


class Meta(type):
    def __new__(self, class_name, baeses, attrs):
        print(attrs)

        attrs['koko'] = 255

        return type(class_name, baeses, attrs)

    def __init__(Class, classname, supers, classdict):
        print('W MetaOne init:', classname, supers, classdict, sep='\n...')
        print('...obiekt zainicjalizowanej klasy:', list(Class.__dict__.keys()))

# Metoda __new__ tworzy i zwraca obiekt klasy, natomiast __init__ inicjalizuje
# już utworzoną, podaną w argumencie klasę.


class Eggs:
    pass


class Spam(Eggs, metaclass=Meta):
    data = 1

    def meth(self, arg):
        return self.data + arg


s = Spam()
s.meth(5)
print(s.koko)

# 1379 dalej to juz tylko dla ciekawości
