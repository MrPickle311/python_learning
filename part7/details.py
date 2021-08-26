# Struktura try/except/else

# try:
#     <instrukcje>                       # Wykonanie najpierw tego głównego działania
# except <nazwa1>:                       # Przechwytuje wszystkie (lub wszystkie pozostałe) typy wyjątków
#     <instrukcje>                       # Wykonane, jeśli nazwa1 zostanie zgłoszona w bloku try
# except (nazwa2, nazwa3):               # Przechwytuje dowolny z wymienionych wyjątków
#     <instrukcje>                       # Wykonane, kiedy wystąpi jeden z tych wyjątków
# except <nazwa4> as <dane>:             # Przechwytuje wymieniony wyjątek oraz jego instancję
#     <instrukcje>                       # Wykonane, jeśli nazwa4 zostaje zgłoszona i zgłoszona zostaje instancja
# except (nazwa1, nazwa2) as wartość:    # Przechwytuje dowolny z wymienionych wyjątków i jego instancję
#     <instrukcje>
# except:                                # Przechwytuje wszystkie (lub wszystkie pozostałe) typy wyjątków
#     <instrukcje>                       # Wykonane dla wszystkich (pozostałych) zgłoszonych wyjątków
# else:
#     <instrukcje>                       # Wykonane, jeśli żaden wyjątek nie został zgłoszony w bloku try


# Przechwy-
# cenie wyjątku o nazwie Exception daje prawie taki sam efekt jak puste except , jednak ignoruje
# wyjątki powiązane z systemowymi wyjściami z programu.

# try:
#   action()
# except Exception:
#   ...

# Kolejność przeszukiwania w bloku 
# try -> except -> else -> finally

# jeśli dostępne jest else , w kodzie musi się znaleźć przynajmniej jedno except

# Przykład zagnieżdżania

sep = '-' * 45 + '\n'

print(sep + 'EXCEPTION RAISED AND CAUGHT')
try:
    x = 'spam'[99]
except IndexError:
    print('except run')
finally:
    print('finally run')
print('after run')


print(sep + 'NO EXCEPTION RAISED')
try:
    x = 'spam'[3]
except IndexError:
    print('except run')
finally:
    print('finally run')
print('after run')


print(sep + 'NO EXCEPTION RAISED, WITH ELSE')
try:
    x = 'spam'[3]
except IndexError:
    print('except run')
else:
    print('else run')
finally:
    print('finally run')
print('after run')


# print(sep + 'EXCEPTION RAISED BUT NOT CAUGHT')
# try:
#     x = 1 / 0
# except IndexError:
#     print('except run')
# finally:
#     print('finally run')
# print('after run')

# W instrukcji raise wyjątki można zgłaszać jako instancje oraz jako klasy

raise IndexError
raise IndexError()

exc = IndexError()
raise exc
excs = [IndexError, TypeError]
raise excs[0]

# instrukcja raise użyta
# bez nazwy wyjątku ani dodatkowych danych po prostu ponownie zgłasza bieżący wyjątek.

try:
    raise IndexError('mielonka')
except IndexError:
    print('przekazywanie')
    raise

# Łańcuchy wyjątków w Pythonie 3.x — raise from

# raise wyjątek from inny_wyjątek

# Kiedy zastosowana zostanie forma z from i jawnie użytą instrukcją raise , drugi wyjątek określa
# inną klasę lub instancję wyjątku, dołączane do atrybutu __cause__ zgłaszanego wyjątku. Jeśli
# zgłoszony wyjątek nie zostanie przechwycony, Python wyświetla oba wyjątki jako części stan-
# dardowego komunikatu o błędzie:

try:
    1 / 0
except Exception as E:
    raise TypeError('Źle!') from E

try:
    try:
        raise IndexError()
    except Exception as E:
        raise TypeError() from E
except Exception as E:
    raise SyntaxError() from E

# Instrukcja assert

def reciprocal(x):
    assert x != 0
    return 1 / x

# Menedżery kontekstu with/as

# Podstawowe zastosowanie

# with wyrażenie [as zmienna]:
#     blok_with

# 1130 