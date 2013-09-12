import sys
from matplotlib import pyplot
from numpy import *
import common
from common import separate_data

# Colores hardcodeados del grafico resultante
colors = ['r', 'g', 'b']      

# atributos, labels, nombre de los labels
def plot(dataset):
    
    (separated_data, plot_data, numpy_data) = common.separate_data(dataset)
    
    
    for i in xrange(0, 3): # Primer atributo = 1,2,3
        for j in xrange(i+1, 4): # Segundo atributo = 2,3,4
            for k in xrange(0, len(plot_data)): # Para cada clase
                pyplot.plot(plot_data[k][i], plot_data[k][j], 'o' + colors[k])
                pyplot.xlabel(str(i+1))
                pyplot.ylabel(str(j+1))
            pyplot.show()


        
    
    
