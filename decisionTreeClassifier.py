from sklearn.tree import DecisionTreeClassifier
import pandas as pd
from modelHelpers import *


def createDecisionTreeModel():
    X_train, X_test, y_train, y_test = getModelData()

    clf = DecisionTreeClassifier().fit(X_train, y_train)

    return clf

def decisionTreeClassifier(state, player):

    clf = createDecisionTreeModel()

    stateLabels = ["1", "2", "3", "4", "5", "6", "7", "8", "9"]
    stateCombined = dict()
    for index, val in enumerate(stateLabels):
        stateCombined[val] = state[index]
    stateDF = pd.DataFrame(stateCombined, index=[0])
    prediction = clf.predict(stateDF)
    # print(prediction)
    if prediction[0] == 'positive':
        return 'X'

    return 'O'

# ************ Testing ******************

# currentPrediction = decisionTreeClassifier([1,1,-1,0,-1,0,1,0,0], 1)
# print(currentPrediction)