import json
import numpy as np
import matplotlib.pyplot as plt

#@feature Compile les scores du BPI: la douleur et l'invalidité
#@vision Affiche ces scores sous forme de graphique

# Ouvre le fichier de type JSON
with open("patient.json") as fichier:
  data = json.load(fichier)

#@cr Compile les scores du BPI et la date et les mets dans des listes

sommesPain = []
sommesInvalidity = []
dates = []

for questionnaire in data["questionnaires"]:
  if questionnaire["name"] == "Brief Pain Inventory":
    reponses = np.array(questionnaire["answers"]).astype(np.int)
    # ajoute le bpi pain a la liste
    sommesPain.append(reponses[[0,1,2,3]].sum())
    # ajoute le bpi invalidité a la liste
    sommesInvalidity.append(reponses[[4,5,6,7,8,9,10]].sum())
    dates.append(questionnaire["time"].split('T')[0])
    

#@cr Affiche les graphiques

plt.subplot(1, 2, 1)
axes = plt.gca()
axes.set_ylim([0,40])
plt.title('Douleur du BPI selon la date')
plt.plot(dates, sommesPain, color='red', marker='o')
plt.xlabel('Date')
plt.ylabel('Douleur')
plt.grid(True)

plt.subplot(1, 2, 2)
axes = plt.gca()
axes.set_ylim([0,70])
plt.title("Invalidité du BPI selon la date")
plt.plot(dates, sommesInvalidity, color='red', marker='o')
plt.xlabel('Date')
plt.ylabel('Invalidité')
plt.grid(True)

plt.tight_layout()
plt.show()