#Bibliotecas, pacotes e funções
''' 
função = max()

Pacote = math(sqrt(),pow(),log(),exp(),sen(),con())

Biblioteca = (math, Módulo 2)

Numpy
    random
        randint, randn, rand

biblioteca   Módulo     função
   numpy.    random.  randint()
'''


import numpy as np

quantidade = [2,5,10,20,35]
custo1 = [100,150,450,320,195]

arr1 = np.array(quantidade)
arr2 = np.array(custo1)

estoque = arr1 * arr2
(estoque)

custo2  = [100,200,300,400]
venda = [125,235,355,490]

arr3 = np.array(custo2)
arr4 = np.array(venda)

lucro = arr4 - arr3

(lucro)
(np.arange(10,101,2,dtype=float))
(np.linspace(1,10,10))

#Random - rand, randn, randint
'''
rand = cria array que segue uma distribuição uniforme, numeros aleatorios entre (0 e 1)
randn = cria array que segue um distribuição normal, media 0 e variancia 1
randint = 
'''
(np.random.rand(10))
(np.random.randn(10))
(np.random.randint(10,100,30))

#como saber se uma array é unidimencional ou bidimencional
#zeros e uns
tabela = np.zeros((3,3),dtype=int)
'''for c in range(3):
    for l in range(3):
        print(tabela[c][l], end=' ')
    print()'''

(np.ones((5,5)))
print(np.eye(6))

