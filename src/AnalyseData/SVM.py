import numpy as np    # pour utiliser des matrices
np.random.seed(7)  # pour la réproductibilité des simulations
import pandas as pd

donnees_data_frame = pd.read_csv('../db/data2015_2016.csv', delimiter=" ")
donnees_ensemble_total = donnees_data_frame.values

donnees_data_frame2 = pd.read_csv('../db/data2012_2015.csv', delimiter=" ")
donnees_ensemble_total2 = donnees_data_frame2.values

nombre_lignes_base = donnees_ensemble_total.shape[0]
nombre_colonnes_base = donnees_ensemble_total.shape[1]

nombre_lignes_base2 = donnees_ensemble_total2.shape[0]
nombre_colonnes_base2 = donnees_ensemble_total2.shape[1]

x_train = donnees_ensemble_total2[0:nombre_lignes_base2, 1:nombre_colonnes_base2 - 4]
y_train = donnees_ensemble_total2[0:nombre_lignes_base2, nombre_colonnes_base2 - 1:]

x_test = donnees_ensemble_total[0:nombre_lignes_base, 1:nombre_colonnes_base - 4]
y_test = donnees_ensemble_total[0:nombre_lignes_base, nombre_colonnes_base - 1:]

#importation de la classe calcul
from sklearn.svm import SVC

svm = SVC(gamma='auto')

print ("\n\n===================\n")

#apprentissage – construction du modèle prédictif
svm.fit( x_train ,y_train)

y_predit_test = svm.predict (x_test)

#evaluation : taux d'erreur
from sklearn import metrics
err = (1.0 -metrics.accuracy_score (y_test ,y_predit_test ))*100
print ("Erreur = ", round (err,2), "%" )
print ("\n\n===================")
