#oque e o numpay
'''
biblioteca de algebra linear para python.
baseado em arrays -> estruturas pra guardar dados -> (lista)(parecido nao igual)

array = [10,20,30,40,50]
indices (0  1  2  3  4)

array so permite um tipo de dado!
'''

#importacao numpy
'''pip install numpy'''

import numpy as np

#primeiros arrays
#arrays apartir de uma lista

quantidade = [2,5,10,20,35]
custo1 = [100,150,450,320,195]

arr1 = np.array(quantidade)
arr2 = np.array(custo1)

estoque = arr1 * arr2
print(estoque)

custo2  = [100,200,300,400]
venda = [125,235,355,490]

arr3 = np.array(custo2)
arr4 = np.array(venda)

lucro = arr4 - arr3
print(lucro)

#arrayes a partir do numpy

#arange()
print(np.arange(10,101,2,dtype=float))

#linspace() = cria um array com números definjidos de elementos
print(np.linspace(1,10,10))
