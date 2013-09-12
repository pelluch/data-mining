from numpy import array
from plot import *
from pca import * 
from fischer import *

def read_data():
    
    # Lectura de archivo
    f = open('../../data/iris.data', 'r')
    lines = f.readlines()
    f.close()
    
    data = []
    labels = []
    label_names = []
    
    for line in lines:
        line = line.rstrip()    # Le quitamos el endline
        separated = line.split(',') # Separacion de atributos
        
        if len(separated) > 1: # Necesario porque hay una linea en blanco al final
            instance = separated[0:4] # Separamos los datos del label
            instance = [float(i) for i in instance] # Transformacion a float
            label = separated[4]
            
            if label not in label_names:
                label_names.append(label)
                
            labels.append(label)
            data.append(instance) # Transformacion a array de numpy
    
    #data = array(data)
    return (data, labels, label_names)
    
def main(argv=None):
    
    # Lectura de archivo
    f = open('../../data/iris.data', 'r')
    lines = f.readlines()
    f.close()
    
    dataset = read_data()
    
    choice = ''
    while choice != 4:
        choice = input('1. Plot data\n2. PCA analysis\n3. Fisher\n4. Exit\n')
        if choice == 1:
            plot(dataset)
        elif choice == 2:
            pca(dataset)
        elif choice == 3:
            fischer(dataset)       
        elif choice == 4:
            return
        else:
            print('Invalid input. Try again.')        

if __name__ == "__main__":
    sys.exit(main())