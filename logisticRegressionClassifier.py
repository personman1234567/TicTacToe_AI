import numpy as np
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import classification_report, confusion_matrix
from minRiskClassifier import *
import pandas as pd
import matplotlib.pyplot as plt

def logisticRegressionClassifier(state, player):
    
    data = pd.read_csv("dataNums.csv")

    stateLabels = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    x = data[stateLabels]
    y = data["class"]
    # stateCombined = dict()
    # for index, val in enumerate(stateLabels):
    #     stateCombined[val] = state[index]
    # stateDF = pd.DataFrame(stateCombined, index=[0])

    # Create Logistic Regression Model
    model = LogisticRegression(random_state=0).fit(x, y)

    # getModelConfusionMatrix(model, x, y)
    # getClassificationReport(model, x, y)

    # Get Next board states
    nextStates = getNextBoardStates(state, player)

    highestProbability = (0,0)
    for key, value in nextStates.items():
        # Format new board state
        stateCombined = dict()
        for index, val in enumerate(stateLabels):
            stateCombined[val] = value[index]
        stateDF = pd.DataFrame(stateCombined, index=[0])

        # Find probability of each new board state
        probabilities = model.predict_proba(stateDF)

        if player == 1:
            if probabilities[0][0] > highestProbability[1]:
                highestProbability = (key, probabilities[0][0])
        else:
            if probabilities[0][1] > highestProbability[1]:
                highestProbability = (key, probabilities[0][1])

    return highestProbability


def getModelConfusionMatrix(model, x, y):
    cm = confusion_matrix(y, model.predict(x))

    fig, ax = plt.subplots(figsize=(8, 8))
    ax.imshow(cm)
    ax.grid(False)
    ax.xaxis.set(ticks=(0, 1), ticklabels=('Predicted Negative', 'Predicted Positive'))
    ax.yaxis.set(ticks=(0, 1), ticklabels=('Actual Negative', 'Actual Positive'))
    ax.set_ylim(1.5, -0.5)
    for i in range(2):
        for j in range(2):
            ax.text(j, i, cm[i, j], ha='center', va='center', color='red')
    plt.show()

def getClassificationReport(model, x, y):
    print(classification_report(y, model.predict(x)))


# prob = logisticRegressionClassifier([1,0,0,0,-1,0,0,0,0], 1)
# print(prob)
