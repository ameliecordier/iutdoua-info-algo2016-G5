#coding: utf8
import numpy as np
import time
from numpy import zeros
from math import sqrt

timings = []

def timefunc(f):
    def f_timer(*args, **kwargs):
        start = time.time()
        result = f(*args, **kwargs)
        end = time.time()
        timeinterval = end - start
        timings.append((f.__name__, timeinterval))
        print(f.__name__, 'took', timeinterval, 'secs')
        return result
    return f_timer


t1alice = np.array([i for i in range(10)])
t2alice = np.array([i for i in range(100)])
t3alice = np.array([i for i in range(1000)])
t4alice = np.array([i for i in range(100000000)])
#t4alice = np.array([i for i in range(100000)])

t1kilian = t1alice[:]
t2kilian = t2alice[:]
t3kilian = t3alice[:]
t4kilian = t4alice[:]

t1thierry = t1alice[:]
t2thierry = t2alice[:]
t3thierry = t3alice[:]
t4thierry = t4alice[:]

def primesfrom2to(n):
    # http://stackoverflow.com/questions/2068372/fastest-way-to-list-all-primes-below-n-in-python/3035188#3035188
    """ Input n>=6, Returns a array of primes, 2 <= p < n """
    sieve = np.ones(n/3 + (n%6==2), dtype=np.bool)
    sieve[0] = False
    for i in range(int((sqrt(n)**0.5)/3)+1):
        if sieve[i]:
            k=3*i+1|1
            sieve[      ((k*k)/3)      ::2*k] = False
            sieve[(k*k+4*k-2*k*(i&1))/3::2*k] = False
    return np.r_[2,3,((3*np.nonzero(sieve)[0]+1)|1)]

#def tagada(tab):
#    primes = primesfrom2to(len(tab)+1)
#    for i in primes:
#        tab[i] = 0




@timefunc
def experimentAlice(array):
    """
    entree array: array
    sortie: array
    post-cond: Remplace toutes les valeurs aux indices premiers du tableau array par 0 et renvoie le nouveau tableau
    """
    size = len(array)
    if size > 2:
        primals = zeros(size)
        output = zeros(size)

        output[0] = array[0]
        output[1] = array[1]

        for j in range(4, size, 2):
            output[j] = array[j]

        for i in range(3, int(sqrt(size)) + 1, 2):
            if primals[i] != 1:
                for j in range(i**2, size, 2*i):
                    primals[j] = 1
                    output[j] = array[j]
    else:
        output = array
    return(output)


@timefunc
def experimentKilian(tab):


    #Micro-ondes
    # Les nombres premiers ne sont pas par definition des multiples d'autres nombres que eux-meme et 1

    longueur = len(tab)

    # On commence donc par presumer que tout les nombres sont premiers donc toutes les valeurs sont égales à 0 dans un nouveau tableau
    tab2 = np.zeros(longueur, dtype=np.int)

    # Il faut maintenant remplacer toutes les valeurs d'indices non premiers par les nombre du tableau d'origine
    if longueur > 0:
        tab2[0] = tab[0]

        if longueur > 1:
            tab2[1] = tab[1]

            if longueur > 4:
                # On commence par tout les multiples de 2
                for multipleDe2 in range(4, longueur, 2):
                    tab2[multipleDe2] = tab[multipleDe2]

                if longueur > 9:
                    # Puis les multiples de 3
                    # la moitié de ces multiples sont egalement des multiples de 2 (6, 12, ...) donc on utilise un pas de 6
                    for multipleDe3 in range(9, longueur, 6):
                        tab2[multipleDe3] = tab[multipleDe3]

                    if longueur > 25:

                        # Maintenant nous devons faire de même pour tout les nombres jusqu'a la racine carre de la longueur
                        # Cependant certaine multiples comme ceux de 4 sont aussi des multiples de 2 donc nous n'avons pas besoins de les refaire

                        # Le reste du code est assez difficile a expliquer sans schema

                        tem = 0

                        for a in range(5, int(longueur**0.5)+2, 2):

                            if tem != 2:

                                if (a-5)%6 == 0:
                                    temp = 0
                                else:
                                    temp = 1

                                for b in range(a, (longueur-1)//a+1, 2):

                                    if temp != 2:
                                        tab2[b*a] = tab[b*a]
                                        temp += 1
                                    else:
                                        temp = 0
                                tem +=1
                            else:
                                tem = 0
    return tab2


@timefunc
def experimentThierry(tab):
    primes = primesfrom2to(len(tab)+1)
    for i in primes:
        tab[i] = 0

r1alice = experimentAlice(t1alice)
r2alice = experimentAlice(t2alice)
r3alice = experimentAlice(t3alice)
r4alice = experimentAlice(t4alice)

r1kilian = experimentKilian(t1kilian)
r2kilian = experimentKilian(t2kilian)
r3kilian = experimentKilian(t3kilian)
r4kilian = experimentKilian(t4kilian)

r1thierry = experimentThierry(t1thierry)
r2thierry = experimentThierry(t2thierry)
r3thierry = experimentThierry(t3thierry)
r4thierry = experimentThierry(t4thierry)

print(timings)

print("Experiment 1 winner")
e1 = timings[0::4]
e1.sort(key=lambda tup: tup[1])
print(e1)

print("Experiment 2 winner")
e1 = timings[1::4]
e1.sort(key=lambda tup: tup[1])
print(e1)

print("Experiment 3 winner")
e1 = timings[2::4]
e1.sort(key=lambda tup: tup[1])
print(e1)

print("Experiment 4 winner")
e1 = timings[3::4]
e1.sort(key=lambda tup: tup[1])
print(e1)


print("Vérification des résultats")
print(False not in (r1alice == r1kilian))
print(False not in (r1alice == t1thierry))
print(False not in (r2alice == r2kilian))
print(False not in (r2alice == t2thierry))
print(False not in (r3alice == r3kilian))
print(False not in (r3alice == t3thierry))
print(False not in (r4alice == r4kilian))
print(False not in (r4alice == t4thierry))



#print((False in (t1alice == t1kilian)) and (False in t1alice == t1thierry))



