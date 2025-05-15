# MUW solution algorithm
import sys
import ast

if len(sys.argv) > 1:
    try:
        v = ast.literal_eval(sys.argv[1])
    except (SyntaxError, ValueError) as e:
        print("Error: El argumento no es una lista válida.")
else:
    print("Error: No se proporcionó argumento.")

# Imprimir v
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
# Allocation X
X = [[] for _ in range(n)]


vec=[0 for i in range(n)]

for k in range(m):
    # vec
    #print('vec =',vec)
    
    # alpha: La utilidad mas grande del item k
    alpha=v[0][k]
    for i in range(n-1):
        if v[i+1][k]>alpha:
            alpha=v[i+1][k]
    #print('alpha =',alpha)
    
    # p: Agentes que tienen la misma utilidad de alpha para el item k
    p=[]
    for i in range(n):
        if v[i][k]==alpha:
            p.append(i+1)
    #print('p =',p)
    
    # l: Busca el valor mas pequeño del vec de cada agente de p
    l=abs(vec[p[0]-1])
    for i in range(len(p)-1):
        #print(l,abs(vec[p[i+1]-1]))
        if abs(vec[p[i+1]-1])<l:
            l=abs(vec[p[i+1]-1])
    #print('l =',l)

    # M: Busca el vec de cada agente de p igual a l y guarda ese agente en M
    M=[]
    for i in range(len(p)):
        #print(l,abs(vec[p[i]-1]))
        if abs(vec[p[i]-1])==l:
            M.append(p[i])
    #print('M =',M)
    
    # J: Selecciona al primer agente en orden 1,...,n
    J=M[0]
    #print('J =',J)
    
    # Asigna el item al agente J
    X[J-1].append(k+1)
    
    # Actualiza vec
    vec[J-1]+=alpha
    print('X =', X)
