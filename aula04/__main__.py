import numpy as np

a = 40
b = 70

print(a>b)

# FORMAS DE SELECIONAR VALORES EM PYTHON

#criasndo a array ...
cadastro = np.random.randint(15,51,size=(50,10))
print(cadastro)

#arr2 com o valor de cadastro > 18 ou seja pra dar True tem q ser maior de 18
cadastro_maior18 = cadastro > 18
print(cadastro_maior18)

#arr3 Essa passa o Cadastro_maior18 como indexação
arr3 = cadastro[cadastro_maior18]
print(len(arr3))

#De uma forma mais direta aq soma todos os valores como False é 0 e True é um somara só os valores maiores de 18 
print(cadastro_maior18.sum())

#aqui é feito com uma condição, usando a função extract passando a contição e o array
print(cadastro)
cond = cadastro>20
extraido = np.extract(cond,cadastro)
