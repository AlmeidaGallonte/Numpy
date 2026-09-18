#Indexação Arrays
'''
    Arrays 
    
    unidimensionais          bidimensionais

    [10,20,30,40,50]         [[10][20][30]
                              [40][50][60]
                              [70][80][90]]

arr[3] = 40               arr[1][1] = 50                     

'''

import numpy as np

'''arr = np.arange(1,11,dtype=int)
print(arr)'''

#indexação unidimencionais

'''print(arr[2:5])'''

#indexação bidimencionais
'''
arr2 = np.random.randint(1,10,size=(3,3))
print(arr2)
print(arr2[0][2])
print(arr2[2][0:2])'''

arr3 = np.random.randint(1,101,size=(10,10))
print(arr3)
print(arr3[2:4,6:9])
print(arr3[[2,4,5]])