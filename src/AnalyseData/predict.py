import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier

donnees_data_frame = pd.read_csv ('../db/data2015_2016.csv' , delimiter=" ")
donnees_ensemble_total= donnees_data_frame.values

nombre_lignes_base=donnees_ensemble_total.shape[0]
nombre_colonnes_base=donnees_ensemble_total.shape[1]

x_train = donnees_ensemble_total[0:round(nombre_lignes_base*3/4),1:donnees_ensemble_total.shape[1]-4]
y_train = donnees_ensemble_total[0:round(nombre_lignes_base*3/4),donnees_ensemble_total.shape[1]-1:]

x_test = donnees_ensemble_total[round(nombre_lignes_base*3/4)+1:,1:donnees_ensemble_total.shape[1]-4]
y_test = donnees_ensemble_total[round(nombre_lignes_base*3/4)+1:,donnees_ensemble_total.shape[1]-1:]

nbr_neurones = 2

nbr_iterations = 20

i = 0
while (i < 10):
    model = MLPClassifier(hidden_layer_sizes=[nbr_neurones], random_state=7, max_iter=nbr_iterations)
    model.fit(x_train, y_train)

    y_pred_train = model.predict(x_train)

    i = i + 1
    nbr_iterations = nbr_iterations + 100

y_pred_test = model.predict(x_test)

plt.clf()
plt.plot(y_test, "b-^", label="à prédire")
plt.plot(y_pred_test, "r:o", label="prédite")
plt.legend()

plt.title("Ensemble TEST - Nombre neurones = " + str(nbr_neurones))

plt.show()

#evaluation : taux d'erreur
from sklearn import metrics
err = (1.0 - metrics.accuracy_score(y_test, y_pred_test))*100
print("Erreur = ", round(err, 2), "%")
print("\n\n===================")