import EF

# Round Robin Algorithm
v=[[0.0426,0.0004,0.1019,0.1503,0.0541,0.1782,0.1212,0.0259,0.1574,0.1681],
   [0.0365,0.0004,0.2311,0.1479,0.0649,0.1150,0.1501,0.1894,0.0285,0.0362],
   [0.1124,0.0972,0.0574,0.0956,0.1441,0.1461,0.0674,0.1272,0.0254,0.1273],
   [0.0368,0.0582,0.0242,0.0784,0.1844,0.1260,0.1124,0.1121,0.1610,0.1064]]

# Ejemplo Goods
v = [[1, 3, 1, 1], [5, 9, 3, 2]]

# Ejemplo Chores
v = [[-7, -9, -7, -5], [-3, -7, -3, -2]]

# G-binary
v = [[1, 3, 0, 0], [1, 3, 1, 1]]
'''
# Ejemplo Mix
v = [[-4, -4, -7, 3], [-1, -1, -4, 1]]
'''

v = [[-4, -4, -7, 3], [-1, -1, -4, 1]]

# Imprimir v
print('v =',v)
print('-----------------')
# Numero de agentes
n=len(v)
#print('|A| =',n)
# Numero de items
m=len(v[0])
#print('|R| =',m)
# Items
R=[i+1 for i in range(m)]
#print('R =',R,'\n')

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

print('--------------')
EF.isEF(X,v,1)
