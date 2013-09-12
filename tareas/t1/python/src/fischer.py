from numpy import *
from numpy.core.numeric import zeros
from numpy.linalg.linalg import inv
import common
from matplotlib import pyplot

def fischer(dataset):
    colors = ['r', 'g', 'b']
    
    labels = dataset[1]
    label_names = dataset[2]
    # Obtenemos el promedio de cada columna
    
    for i in xrange(len(label_names)): # Para cada clase de hace un one vs all
        c1 = label_names[i]
        new_labels = []
        
        # Se crean nuevos labels para las clases: 0 y 1
        for label in labels:
            if label == c1:
                new_labels.append(0)
            else:
                new_labels.append(1)
        
        # Separacion de datos, nuevamente
        (separated_data, tranposed, data) = common.separate_data((dataset[0], new_labels, [0, 1]))
        #Calculo de medias
        means = [ separated_data[0].mean(0), separated_data[1].mean(0) ]
        
        # inicializamos las matrices de scatter
        s1 = [[0,0,0,0], [0,0,0,0],[0,0,0,0],[0,0,0,0]]
        s2 = [[0,0,0,0], [0,0,0,0],[0,0,0,0],[0,0,0,0]]
        
        # Simplemente sacamos los scatters
        for row in separated_data[0]:
            m1 = array([row- means[0]])
            m2 = array([row- means[0]]).transpose()
            s1 = s1 + dot(m2, m1)
            
        for row in separated_data[1]:
            m1 = array([row- means[1]])
            m2 = array([row- means[1]]).transpose()
            s2 = s2 + dot(m2, m1)
        
        # Within class scatter
        sw = s1 + s2
        inv_sw = inv(sw)
        mean_diff = array([means[0]-means[1]]) # mu1 - mu2, es necesario llevarlo a un "doble arreglo" para multiplicar matrices
        
        # Esta sera la direccion v optima
        direction = dot(inv_sw, mean_diff.T)
        
        p1 = [[],[]]
        
        for idx, row in enumerate(data):        
            p1[[0, 1].index(new_labels[idx])].append(dot(row,direction))
        
        # Ploteamos los datos proyectados
        print('Rojo: ' + c1)
        print('Azul: las otras')
        pyplot.plot(p1[0], zeros(len(p1[0])), 'or')
        pyplot.plot(p1[1], zeros(len(p1[1])), 'ob')
        pyplot.show()
    
    
        
       
        