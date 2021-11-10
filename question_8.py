from sklearn import datasets, neighbors, metrics, svm
from sklearn.model_selection import train_test_split

dataset = datasets.load_iris()
print(dataset)

X = dataset.data
print('Array of data samples:')
print(X)
print()
n_samples, n_features = X.shape

print('Number of data samples: ', n_samples)
print('Dimensionality (Number of features): ', n_features)
print()
y = dataset.target
print('True class index of data samples:')
print(y)
print()
class_names = dataset.target_names
print('Array of class names:', class_names)
print('Number of classes:', len(class_names))
print()

# Split dataset into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.25, random_state=0)
print(X_train)
print()
print(X_test)
print()
print(y_train)
print()
print(y_test)
print()

# Load classifier containing classification technique and model
classifier = neighbors.KNeighborsClassifier(n_neighbors=3)

# Training
classifier.fit(X_train, y_train)
# Testing
y_pred = classifier.predict(X_test)


def get_confusion_matrix(true_list, predicted_list, class_labels):
    c_matrix = metrics.confusion_matrix(true_list, predicted_list)
    print(f"%35s" % " ", end='')
    for i in class_labels:
        print(f"%35s" % i, end='')
    print()
    p = 0
    for i in c_matrix:
        print(f"%35s" % class_labels[p], end='')
        for j in i:
            print(f"%35s" % j, end='')
        print()
        p = p + 1

    return c_matrix


label_names = ['Setosa', 'Versicolour', 'Virginica']
confusion_matrix = get_confusion_matrix(y_pred, y_test, label_names)
