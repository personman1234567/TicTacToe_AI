import numpy as np
from sklearn.linear_model import LogisticRegression
import pandas as pd
from modelHelpers import *

def createLogisticRegressionModel():
    X_train, X_test, y_train, y_test = getModelData()

    lrm = LogisticRegression().fit(X_train, y_train)

    return lrm

def logisticRegressionClassifier(state, player):
    
    model = createLogisticRegressionModel()

    # Get Next board states
    nextStates = getNextBoardStates(state, player)

    stateLabels = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
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





# prob = logisticRegressionClassifier([1,0,0,0,-1,0,0,0,0], 1)
# print(prob)
