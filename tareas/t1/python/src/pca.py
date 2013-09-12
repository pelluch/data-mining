import sys
from plot import *
from matplotlib import pyplot
from numpy import *
import common

def pca(dataset):
    
    colors = ['r', 'g', 'b']
    
    labels = dataset[1]
    label_names = dataset[2]
    # Obtenemos el promedio de cada columna
    
    (separated_data, tranposed, data) = common.separate_data(dataset)
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
    
    # Datos proyectados en distintas direcciones
    projected_data_1 = [[], [], []]
    projected_data_2 = [[], [], []]
    
    for idx, row in enumerate(data):        
        projected_data_1[label_names.index(labels[idx])].append(dot(row,first_pc))
    
    for idx, row in enumerate(data):        
        projected_data_2[label_names.index(labels[idx])].append(dot(row,second_pc))

    label_names = [ 'Iris-setosa' , 'Iris-versicolor' , 'Iris-virginica' ]
    
    # Ploteo con solo un PC
    for i in xrange(len(colors)-1):
        for j in xrange(i+1, len(colors)):            
            pyplot.plot(projected_data_1[i], zeros(len(projected_data_1[i])), 'o' + colors[i])
            pyplot.plot(projected_data_1[j], zeros(len(projected_data_1[j])), 'o' + colors[j])
            print('Clase ' + colors[i] + ": " + label_names[i])
            print('Clase ' + colors[j] + ": " + label_names[j])
            pyplot.show()
    
    # Dos PC
    for i in xrange(len(colors)-1):
        for j in xrange(i+1, len(colors)):
            pyplot.plot(projected_data_1[i], projected_data_2[i], 'o' + colors[i])
            pyplot.plot(projected_data_1[j], projected_data_2[j], 'o' + colors[j])
            print('Clase ' + colors[i] + ": " + label_names[i])
            print('Clase ' + colors[j] + ": " + label_names[j])
            pyplot.show()
    
    # Igual que lo anterior, pero con 3 clases
    for i in xrange(len(colors)):
        pyplot.plot(projected_data_1[i], projected_data_2[i], 'o' + colors[i])
        print('Clase ' + colors[i] + ": " + label_names[i])
    pyplot.show()