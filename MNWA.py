# MNW solution algorithm
from itertools import permutations
import MS
import math
import sys
import ast

if len(sys.argv) > 1:
    try:
        v = ast.literal_eval(sys.argv[1])
    except (SyntaxError, ValueError) as e:
        print("Error: El argumento no es una lista válida.")
else:
    print("Error: No se proporcionó argumento.")

def isUPositive(agentes,allo,v):
    if len(agentes)==0:
        flag=1
    else:
        flag=0
    for i in range(len(agentes)):
        utility=0
        for j in range(len(allo[agentes[i]-1])):
            #print('aaaaa',agentes[i],allo[agentes[i]-1][j],allo)
            utility+=v[agentes[i]-1][allo[agentes[i]-1][j]-1]
        #print('utility =',round(utility,4))
        if round(utility,4)<=0:
            flag=1
            break
    return flag

# Calcula la utilidad dado una lista de agentes, una asignacion y un v
def utility_allocation_agents(agentes,allo,v):
    #print('Agentes = ',agentes)
    aux=[]
    for i in range(len(agentes)):
        utility=0
        for j in range(len(allo[i])):
            #print(agentes[i],allo[i][j],allo)
            utility+=v[agentes[i]-1][allo[i][j]-1]
        aux.append(round(utility,4))
    return round(math.prod(aux),4)

# -----------------------------------------------------------------------------
print('v =',v)
print('-----------')
# Numero de agentes
n=len(v)
# Agentes
A=[i+1 for i in range(n)]
print('A =',A)
# Numero de items
m=len(v[0])
# Items
R=[i+1 for i in range(m)]
print('R =',R)
print('-----------')
# -----------------------------------------------------------------------------
# Set de agentes 2^{A}
TwotoA=MS.makesetsall(A)

# Set de recursos A^{R}
AtoR=MS.makesetsall(R)
PermuOfAtoR=list(permutations(AtoR,n)) # Set de asignaciones validas y no validas

# Guardar asignaciones validas
Allocations=[]
for i in PermuOfAtoR:
    aux=[]
    for j in i:
        aux+=j
    aux.sort()
    # Filtro asignaciones validas
    if aux==R:
        Allocations.append(i)

# Tuplas a listas
PermuOfAtoR_new=[]
for i in Allocations:
    #print(i)
    aux_tuple_to_list=[]
    for j in i:
        aux_tuple_to_list.append(list(j))
    #print(aux_tuple_to_list)
    PermuOfAtoR_new.append(aux_tuple_to_list)
Allocations=PermuOfAtoR_new
# -----------------------------------------------------------------------------
S=[]
for i in TwotoA:
    #print(i)
    for allo in Allocations:
        #print('allo = {} | {}'.format(allo, isUPositive(i,allo,v)))
        if isUPositive(i,allo,v)==0:
            #print('allo = {} | {}'.format(allo, isUPositive(i,allo,v)))
            S.append(i)
            break
    #print('-------------')
flag=0
if len(S)!=0 and len(S[0])==n:
    S=S[0]
    print('S =',S)
else:
    print('No existe asignación donde todos los agentes tengan utilidad positiva')
    flag=1
# -----------------------------------------------------------------------------
if flag!=1:
    # Crear asignaciones de los agentes en S
    PermuOfAtoR=list(permutations(AtoR,len(S)))
    # Guardar asignaciones validas
    Allocations=[]
    for i in PermuOfAtoR:
        aux=[]
        for j in i:
            aux+=j
        aux.sort()
        # Filtro asignaciones validas
        if aux==R:
            Allocations.append(i)
    # Tuplas a listas
    PermuOfAtoR_new=[]
    for i in Allocations:
        #print(i)
        aux_tuple_to_list=[]
        for j in i:
            aux_tuple_to_list.append(list(j))
        #print(aux_tuple_to_list)
        PermuOfAtoR_new.append(aux_tuple_to_list)
    Allocations=PermuOfAtoR_new

    # Encontrar el MNW del conjunto de asignaciones de S
    aux_max_nash=utility_allocation_agents(S,i,v)
    for i in Allocations:
        #print(i,utility_allocation_agents(S,i,v))
        if utility_allocation_agents(S,i,v)>aux_max_nash:
            aux_max_nash=utility_allocation_agents(S,i,v)
    print('-------------')
    for i in Allocations:
        if utility_allocation_agents(S,i,v)==aux_max_nash:
            # Allocation X
            X = [[] for _ in range(n)]
            print('Aux = {} | MNSW = {}'.format(i,utility_allocation_agents(S,i,v)))
            # Llena X
            index=0
            for agent in S:
                #print(agent-1)
                X[agent-1]=i[index]
                index+=1
            print('X =',X)
else:
    None
