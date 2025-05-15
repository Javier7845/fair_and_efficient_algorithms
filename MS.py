from itertools import combinations,permutations

# Dada una lista la siguiente funcion hace una lista de listas que contiene
# todas las combinaciones de la lista dada. Si el tamaño de la lista es
# diferente de 1 la lista no incluira el elemento vacio caso contrario si
# la incluira.

def makesetsall(X):
    i=len(X)
    comb=[]
    while i!=-1:
        txt=list(combinations(X,i))
        for j in range(len(txt)):
            comb.append(txt[j])
        i-=1
    return comb

def makesets(X):
    i=len(X)
    comb=[]
    while i!=len(X)-2:
        txt=list(combinations(X,i))
        for j in range(len(txt)):
            comb.append(txt[j])
        i-=1
    return comb
