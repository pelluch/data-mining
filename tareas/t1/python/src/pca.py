import sys
from plot import *
from matplotlib import pyplot
from numpy import *

def pca(data, labels):
    
    # Obtenemos el promedio de cada columna
    means = data.mean(0)
    std_data = data - means;
    # Obtenemos la matriz de covarianza
    cov_mat = cov(std_data.T)
    [values, vectors] = linalg.eig(cov_mat)
    tuples = []
    
    for i in xrange(len(values)):
        tuples.append((values[i], vectors[i]))
    
    sorted(tuples)
    first_pc = tuples[0][1]
    second_pc = tuples[1][1]
    projected_data = [[], []]
    
    for instance in data:
        projected_data[0].append(dot(first_pc, instance))
    
    for instance in data:
        projected_data[1].append(dot(second_pc, instance))
        
        
    separated_data = [[], [], []]
    #print projected_data
    labels_map = { 'Iris-setosa' : 0, 'Iris-versicolor' : 1, 'Iris-virginica' : 2 }
    
    for i in xrange(len(labels)):
        separated_data[labels_map[labels[i]]].append(projected_data[labels_map[labels[i]]])
        
    
    
    print separated_data
    #------------------------------------------------------ print separated_data
    #-------------------------------------- pyplot.plot(separated_data[0], 'ro')
    #-------------------------------------- pyplot.plot(separated_data[1], 'go')
    #-------------------------------------- pyplot.plot(separated_data[2], 'bo')
    #------------------------------------------------------------- pyplot.show()
    #print separate_by_class(projected_data, labels)[0]
    #print labels
    
    #print tuples
    
    #for vector in vectors:
    #print cov_mat