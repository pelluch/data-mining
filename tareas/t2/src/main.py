import sys
import numpy
from sklearn import neighbors
from sklearn import cross_validation
from sklearn import metrics
from sklearn.tree import DecisionTreeClassifier
from sklearn.naive_bayes import GaussianNB

from prettytable import PrettyTable

#import data

data_path = '../data/data.txt'

def main():

    print('<head><link rel="stylesheet" type="text/css" href="style.css"></head>')
    with open(data_path, 'r') as data_file:
        headers = data_file.readline().split(' ')
        dtypes = []

        data = numpy.loadtxt(data_file,
                             usecols=range(1, len(headers)))
        labels = data[:, -1]
        features = data[:, :-1]
        nearest_neighbours(features, labels)
        decision_trees(features, labels)
        naive_bayes(features, labels)

def naive_bayes(features, labels):
    classifier = GaussianNB()
    classifier.fit(features, labels)
    scores = cross_validation.cross_val_score(classifier, features, labels, cv=10,
                                      score_func=metrics.precision_recall_fscore_support)
    print_table('Naive Bayes', numpy.around(numpy.mean(scores, axis=0), 2))

def print_table(header, scores):
        print('<br/>' + header)
        t = PrettyTable(['Precision', 'Recall', 'Fscore'])
        for label in range(8):
            t.add_row(scores[:-1, label])
        print(t.get_html_string())

def nearest_neighbours(features, labels):
    num_neighbours = [5, 8, 15]
    knn_scores = []
    for idx, k in enumerate(num_neighbours):
        classifier = neighbors.KNeighborsClassifier(k)
        distances = classifier.fit(features, labels)
        scores = cross_validation.cross_val_score(classifier, features, labels, cv=10,
                                                  score_func=metrics.precision_recall_fscore_support)

        print_table('KNN ' + str(k), numpy.around(numpy.mean(scores, axis=0), 2))


def decision_trees(features, labels):
    classifier = DecisionTreeClassifier(random_state=0, criterion='entropy')
    classifier.fit(features, labels)
    scores = cross_validation.cross_val_score(classifier, features, labels, cv=10,
                                              score_func=metrics.precision_recall_fscore_support)
    print_table('Decision Trees', numpy.around(numpy.mean(scores, axis=0), 2))

if  __name__ == '__main__':
    sys.exit(main())