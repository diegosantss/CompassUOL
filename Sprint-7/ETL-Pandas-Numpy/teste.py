import numpy as np

tupla = ('a', 'b', 'c', 'd')
lista = [1,2,3,6,7,9,12]

array1 = np.arange(10)
array2 = np.arange(2,5)
array3 = np.arange(5, dtype=np.float32)

print("Conteúdo:{}, shape: {}, tipo: {}".format(array1, array1.shape, array1.dtype))
print("Conteúdo:{}, shape: {}, tipo: {}".format(array2, array2.shape, array2.dtype))

print("Conteúdo:{}, shape: {}, Tipo: {}".format(array3, array3.shape, array3.dtype))