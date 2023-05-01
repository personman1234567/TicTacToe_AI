import numpy as np
from sklearn.linear_model import LogisticRegression
from minRiskClassifier import *
import pandas as pd

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

        if probabilities[0][0] > highestProbability[1]:
            highestProbability = (key, probabilities[0][0])
        # print(probabilities[0][0])
        # print(probabilities[0][1])

    return highestProbability




# prob = logisticRegressionClassifier([1,0,0,0,-1,0,0,0,0], 1)
# print(prob)
