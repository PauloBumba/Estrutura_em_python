matriz=matrix=[[0,0,0]
        ,[0,0,0],
        [0,0,0]]
for c in range(3):
    for j in range(3):
        matriz[c][j]=int(input(f"informe um valor na posição[{c,j}] da matriz"))
        print(matriz)
for c in range(3):
    for j in range(3):
        print(f'[{matrix[c][j]: ^5}]',end='')
    print( )
    