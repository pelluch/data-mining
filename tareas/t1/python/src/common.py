from numpy import *

# Crea un arreglo de matrices con los datos separados y lo retorna
# atributos, labels, nombre de los labels

def separate_data(dataset):
    
    separated_data = [ [] for i in dataset[2] ]
    transposed = [ [] for i in dataset[2] ]
    
    for idx, row in enumerate(dataset[0]):
        separated_data[dataset[2].index(dataset[1][idx])].append(row)
    
    separated_data = [ array(i) for i in separated_data ]
    transposed = [ m.transpose() for m in separated_data ]
    numpy_data = array(dataset[0])
    
    return (separated_data, transposed, numpy_data)