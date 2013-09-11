import sys
from matplotlib import pyplot
from numpy import *

def separate_by_class(data, labels):
    separated_data = [[], [], []]
    labels_map = { 'Iris-setosa' : 0, 'Iris-versicolor' : 1, 'Iris-virginica' : 2 }
    
    for i in xrange(len(labels)):
        separated_data[labels_map[labels[i]]].append(data[i])
    
    return separated_data

def plot(data):
    
    # Colores hardcodeados del grafico resultante
    colors = ['r', 'g', 'b']        
    plot_data = [row.transpose() for row in data]
    
    for i in xrange(0,3): # Primer atributo = 1,2,3
        for j in xrange(i+1, 4): # Segundo atributo = 2,3,4
            for k in xrange(0, len(plot_data)): # Para cada clase
                pyplot.plot(plot_data[k][i], plot_data[k][j], 'o' + colors[k])
                pyplot.xlabel(str(i+1))
                pyplot.ylabel(str(j+1))
            pyplot.show()


        
    
    
