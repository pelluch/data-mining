from numpy import array
from plot import *
from pca import * 
from fischer import *

def main(argv=None):
    
    # Lectura de archivo
    f = open('../../data/iris.data', 'r')
    lines = f.readlines()
    f.close()
    
    data = []
    separated_data = [[], [], []] # Lista de matrices
    labels_map = { 'Iris-setosa' : 0, 'Iris-versicolor' : 1, 'Iris-virginica' : 2 }
    #labels = [0, 1, 2]
    labels = []
    for line in lines:
        line = line.rstrip()    # Le quitamos el endline
        separated = line.split(',') # Separacion de atributos
        
        if len(separated) > 1: # Necesario porque hay una linea en blanco al final
            current_instance = separated[0:4] # Separamos los datos del label
            current_instance = [float(i) for i in current_instance] # Transformacion a float
            label = separated[4]
            labels.append(label)
            data.append(array(current_instance))
            separated_data[labels_map[label]].append(array(current_instance))
    
    separated_data = [array(row) for row in separated_data]
    data = array(data)
    
    choice = ''
    while choice != 4:
        choice = input('1. Plot data\n2. PCA analysis\n3. Exit\n')
        if choice == 1:
            plot(separated_data)
        elif choice == 2:
            pca(data, labels, labels_map)
        elif choice == 3:
            fischer(data, labels, labels_map)       
        elif choice == 4:
            return
        else:
            print('Invalid input. Try again.')
        

if __name__ == "__main__":
    sys.exit(main())