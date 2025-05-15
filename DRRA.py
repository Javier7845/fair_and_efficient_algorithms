# Double Round Robin algorithm
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

# --------------------------------------------------------------------
# Crea R^{-} y R^{+}
aux=[]
Rp=[]
Rn=[]

for item in range(m):
    flag=v[0][item]
    for i in range(n-1):
        #print(v[i+1][item],flag)
        if v[i+1][item]>flag:
            flag=v[i+1][item]
        #print(flag)
    if flag>0:
        Rp.append(item+1)
    else:
        Rn.append(item+1)
# --------------------------------------------------------------------
# Calcula g
if len(Rn)==0:
    g=0
else:
    i=1
    g=-1
    while g<0:
        g=i*n-len(Rn)
        i+=1
print('g =',g)

# Crea g dummies
d=m
for i in range(g):
    d+=1
    Rn.append(d)
# Crea el dummy en v
for i in range(n):
    v[i].append(0)
               
print('Rp =',Rp)
print('Rn =',Rn)
print('-----------')
# --------------------------------------------------------------------
# Round Robin con Rn
aux_list=[]
for k in range(len(Rn)):
    j=k%n
    # Item maximo del agente j
    max_value=-9999999999
    index=0
    for item in range(len(Rn)):
        if v[j][Rn[item]-1]>max_value and Rn[item] not in aux_list:
            max_value=v[j][Rn[item]-1]
            index=item
    X[j].append(Rn[index])
    print('X =',X)
    aux_list.append(Rn[index])
print('-----------------------')
# --------------------------------------------------------------------
# Round Robin con Rp
aux_list=[]
for k in range(len(Rp)):
    j=(n - k % n - 1) % n
    # Item maximo del agente j
    max_value=-9999999999
    index=0
    for item in range(len(Rp)):
        if v[j][Rp[item]-1]>max_value and Rp[item] not in aux_list:
            max_value=v[j][Rp[item]-1]
            index=item
    X[j].append(Rp[index])
    print('X =',X)
    aux_list.append(Rp[index])
print('-----------------------')
# --------------------------------------------------------------------
# Elimino los dummies que se asignaron en la fase negativa

# Allocation X
X_final = [[] for _ in range(n)]

for agent in range(n):
    for item in range(len(X[agent])):
        if X[agent][item] in R:
            X_final[agent].append(X[agent][item])
X=X_final
print('X =',X)
