from itertools import permutations
import MS, EF
import math

# Funcion retorna 0 si todas las utilidades son positivas caso contrario 0
# Input: Agentes, asignacion, v
# Output: 0 o 1

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

'''
# Ejemplo
v=[[0.1,0.2,0.3],
   [1,2,3]]
X=[[], [3]]
agentes=(2,1)
print(isUPositive(agentes,X,v))
'''

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
# Ejemplo Goods
v = [[1, 3, 1, 1], [5, 9, 3, 2]]

# Ejemplo Chores
v = [[-7, -9, -7, -5], [-3, -7, -3, -2]]

# Ejemplo Mix
v = [[-4, -4, -7, 3], [-1, -1, -4, 1]]


v = [[-9, 0, 0, 2], [0, 2, -4, 2]]


'''

v=[[500,200, 50, 0,   0],
   [500,0,   50, 100, 250],
   [500,200, 0,  100, 0]]

v=[[1,1],
   [2,3],
   [4,5]]

v=[[2,1,3,4],
   [0,0,0,0]]

v=[[2,0,0,0],
   [2,0,0,0]]

v=[[20,1,1,1,1,1,1,1,1,1,1,1.3,1.3,1.3,1.3,1.3,1.3,1.3,1.3,1.3,1.3,1.3,1.3,1.3,1.3,1.3,1.3,1.3,1.3,1.3,1.3],
   [15,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1,1.3,1.3,1.3,1.3,1.3,1.3,1.3,1.3,1.3,1.3],
   [10,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,0,1,1,1,1,1,1,1,1,1,1]]
'''
print('v =',v)
print('-----------')
# Numero de agentes
n=len(v)
#print('|A| =',n)
# Agentes
A=[i+1 for i in range(n)]
print('A =',A,'\n')
# Numero de items
m=len(v[0])
#print('|R| =',m)
# Items
R=[i+1 for i in range(m)]
print('R =',R,'\n')
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
'''
print('TwotoA =',TwotoA)
print('Allocations =',Allocations)
print('\n')
'''
S=[]
for i in TwotoA:
    print(i)
    for allo in Allocations:
        #print('allo = {} | {}'.format(allo, isUPositive(i,allo,v)))
        if isUPositive(i,allo,v)==0:
            print('allo = {} | {}'.format(allo, isUPositive(i,allo,v)))
            S.append(i)
            break
    print('-------------')
print('S =',S)
if len(S)!=0:
    S=S[0]
else:
    print('No hay agente(s) para la cual su utilidad es positiva')
#print('S =',S)

# -----------------------------------------------------------------------------
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
        print('S =',S)
        print('P. Allocation = {} | MNW = {}'.format(i,utility_allocation_agents(S,i,v)))
        # Llena X
        index=0
        for agent in S:
            #print(agent-1)
            X[agent-1]=i[index]
            index+=1
        print('X =',X)
        print('-------------')
# Llena de vacios los agentes que no estan en S
EF.isEF(X,v,1)
