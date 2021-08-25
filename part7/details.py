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

# Część try/else 1115




