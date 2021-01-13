import numpy as np
import pandas as pd
from sklearn import metrics
from sklearn.utils import column_or_1d

np.random.seed(7)
import matplotlib.pyplot as plt
from sklearn.neural_network import MLPClassifier

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

y_test  =  column_or_1d (y_test, warn=False)
y_train  =  column_or_1d (y_train, warn=False)

y_booker = []
k = 0

while k < nombre_lignes_base:

    reponse = min(donnees_ensemble_total[k, (nombre_colonnes_base - 4)], donnees_ensemble_total[k, (nombre_colonnes_base - 3)], donnees_ensemble_total[k, (nombre_colonnes_base - 2)])
    if reponse == donnees_ensemble_total[k, (nombre_colonnes_base - 4)]:
        y_booker.append(0)
    elif reponse == donnees_ensemble_total[k, (nombre_colonnes_base - 3)]:
        y_booker.append(1)
    else:
        y_booker.append(2)
    k += 1

nbr_neurones = 6

nbr_iterations = 1

i = 0
while i < 7:
    model = MLPClassifier(hidden_layer_sizes=[nbr_neurones], alpha=0.05, random_state=7, max_iter=nbr_iterations)
    model.fit(x_train, y_train)

    y_predit_train = model.predict(x_train)
    y_predit_test = model.predict(x_test)

    '''if i == 0:
        tableau_erreurs_train = np.array(100 - metrics.accuracy_score(y_train, y_predit_train) * 100)
        tableau_erreurs_test = np.array(100 - metrics.accuracy_score(y_test, y_predit_test) * 100)
    else:
        tableau_erreurs_train = np.append(tableau_erreurs_train,
                                          100 - metrics.accuracy_score(y_train, y_predit_train) * 100)
        tableau_erreurs_test = np.append(tableau_erreurs_test,
                                         100 - metrics.accuracy_score(y_test, y_predit_test) * 100)'''

    i = i + 1
    nbr_iterations += 10

#plt.plot(tableau_erreurs_train, label="train")
#plt.plot(tableau_erreurs_test, label="test")
#plt.legend()
#plt.title("Taux d'erreur avec " + str(nbr_iterations) + " itérations en fonction du nombre de neurones")
#plt.show()

y_pred_test = model.predict(x_test)

argent = 0
argent2 = 0

for j in range(0, len(y_pred_test)):
    if int(y_pred_test[j]) == 1:
        if int(y_test[j]) == int(y_pred_test[j]):
            argent += 10*(donnees_ensemble_total[j, nombre_colonnes_base - 3]-1)
        else:
            argent -= 10

for j in range(0, len(y_pred_test)):
    if int(y_pred_test[j]) == 0:
        if int(y_test[j]) == int(y_pred_test[j]):
            argent2 += 10*(donnees_ensemble_total[j, nombre_colonnes_base - 4]-1)
        else:
            argent2 -= 10
    elif int(y_pred_test[j]) == 1:
        if int(y_test[j]) == int(y_pred_test[j]):
            argent2 += 10*(donnees_ensemble_total[j, nombre_colonnes_base - 3]-1)
        else:
            argent2 -= 10
    else:
        if int(y_test[j]) == int(y_pred_test[j]):
            argent2 += 10*(donnees_ensemble_total[j, nombre_colonnes_base - 2]-1)
        else:
            argent2 -= 10

argent_booker = 0

for j in range(0, len(y_booker)):
    if int(y_booker[j]) == 0:
        if int(y_test[j]) == int(y_booker[j]):
            argent_booker += 10*(donnees_ensemble_total[j, nombre_colonnes_base - 4]-1)
        else:
            argent_booker -= 10
    elif int(y_booker[j]) == 1:
        if int(y_test[j]) == int(y_booker[j]):
            argent_booker += 10*(donnees_ensemble_total[j, nombre_colonnes_base - 3]-1)
        else:
            argent_booker -= 10
    else:
        if int(y_test[j]) == int(y_booker[j]):
            argent_booker += 10*(donnees_ensemble_total[j, nombre_colonnes_base - 2]-1)
        else:
            argent_booker -= 10

print("Si vous nous aviez suivi sur les nuls, vous auriez actuellement gagné "+str(round(argent, 2))+"€")

print("Si vous nous aviez suivi sur tous nos paris, vous auriez actuellement gagné "+str(round(argent2, 2))+"€")

print("Si vous aviez suivi les bookmakers, vous auriez actuellement "+str(round(argent_booker, 2))+"€")
print("\n===================")

nb_total = 0
bien_predit = 0

for j in range(0, len(y_test)):
    if int(y_test[j]) == 1:
        nb_total += 1
        if int(y_test[j]) == int(y_pred_test[j]):
            bien_predit += 1

print("Taux d'erreur sur les nuls : "+str(round((1-(bien_predit/nb_total))*100, 2))+"%")
print("\n===================")

'''plt.clf()
plt.plot(y_test, "b-^", label="à prédire")
plt.plot(y_pred_test, "r:o", label="prédite")
plt.legend()

plt.title("Ensemble TEST - Nombre neurones = " + str(nbr_neurones))
# plt.get_current_fig_manager().window.state('zoomed')
plt.show()'''

# evaluation : taux d'erreur
from sklearn import metrics

err = (1.0 - metrics.accuracy_score(y_test, y_pred_test)) * 100
print("Erreur entre prédiction et résultat = ", round(err, 2), "%")
print("\n===================")
erreur = (1.0 - metrics.accuracy_score(y_booker, y_test)) * 100
print("Erreur entre résultat et bookmaker = ", round(erreur, 2), "%")
print("\n===================")
erreur = (1.0 - metrics.accuracy_score(y_booker, y_pred_test)) * 100
print("Erreur entre prédiction et bookmaker= ", round(erreur, 2), "%")
print("\n===================")