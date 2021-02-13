import time, math, sys, timeit

timer = time.perf_counter

def total(reps, func, *pargs, **kargs):
    repslist = list(range(reps))
    start = timer()
    for i in repslist:
        ret = func(*pargs,**kargs)
    elapsed = timer() - start
    return (elapsed,ret)

def bestof(reps, func, *pargs, **kargs):
    best = 2 ** 32
    for i in range(reps):
        start = timer()
        ret = func(*pargs,**kargs)
        elapsed = timer() - start
        if elapsed < best : best = elapsed
    return (best,ret)

def bestoftotal(reps1,reps2,func,*pargs,**kargs):
    return bestof(reps1,total,reps2,func,*pargs,**kargs)

#print(total(10000,math.pow,500,40))
#print(bestof(1000,math.pow,2,1000))
#print(bestoftotal(50, 1000, str.upper, 'spam'))

reps = 10000
repslist = list(range(reps))

def forLoop():
    res = []
    for x in repslist:
        res.append(abs(x))
    return res

def listComp(): return [abs(x) for x in repslist]
def mapCall():
    return list(map(abs,repslist))
def genExpr():
    return list(abs(x) for x in repslist)
def genFunc():
    def gen():
        for x in repslist:
            yield abs(x)
    return list(gen())

#for test in [forLoop,listComp,mapCall,genExpr,genFunc]:
#    (bestof,(total,result)) = bestoftotal(5,1000,test)
#    print('%-9s: %.5f  -> [%s...%s]' % (test.__name__,bestof,result[0],result[-1]))

# for test in (forLoop, listComp, mapCall, genExpr, genFunc):
#     (bestof, (total, result)) = bestoftotal(5, 1000, test)
#     print ('%-9s: %.5f => [%s...%s]' % (test.__name__, bestof, result[0], result[-1]))
    
#jednak do testowania wydajności służy moduł timeit

print(min(timeit.repeat(stmt="[x ** 2 for x in range(1000)]",number=1000,repeat=5)))
#                               wykonaj ten blok            1000 razy   po 5 próbek i zwróć czas najszybciej wykonanej próbki min()

#wielowierszowe operacje

min(timeit.repeat(number=1000,repeat=5,
                  stmt="L = [1,2,3,4] \nfor i in L: i += 5"))

#kod instalacyjny tzn. taki ,który konfiguruje nam wstępnie dane, lecz nie jest liczony do czasu wykonywania operacji

print(min(timeit.repeat(number=1000,repeat=5,
                  setup='import math\n'
                        'vals=list(range(1000))',
                  stmt='for x in vals: math.sqrt(x)')))

#ale również można tam załadować funkcję xd
def testcase():
    y = [x ** 5 for x in range(1000)]
print(min(timeit.repeat(stmt=testcase,number=1000,repeat=3)))
print(min(timeit.repeat(stmt=testcase,number=1000,repeat=3)))
print(min(timeit.repeat(stmt=testcase,number=1000,repeat=3)))