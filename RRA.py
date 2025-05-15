# Round Robin algorithm
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
#print('|R| =',m)
# Items
R=[i+1 for i in range(m)]
print('R =',R)
print('-----------')
# Allocation X
X = [[] for _ in range(n)]

aux_list=[]
for k in range(m):
    j=k%n
    # Item maximo del agente j
    max_value=-9999999999
    index=0
    for item in range(m):
        if v[j][R[item]-1]>max_value and R[item] not in aux_list:
            max_value=v[j][R[item]-1]
            index=item
    X[j].append(R[index])
    print('X =',X)
    aux_list.append(R[index])
