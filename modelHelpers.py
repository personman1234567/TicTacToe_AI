# Imports
import pandas as pd
from sklearn.model_selection import train_test_split
import copy
import matplotlib.pyplot as plt
from sklearn.metrics import classification_report, confusion_matrix

def getModelData():
    data = pd.read_csv("data/dataNums.csv")  

    X = data.drop("class", axis=1)
    y = data["class"]

    return train_test_split(X, y, test_size=0.3, random_state=42)

# Get all the next possible board states for the given player
def getNextBoardStates(state, player):
    states = dict()

    # Loop through current board state
    for i, val in enumerate(state):
        tempState = copy.copy(state)
        # For each 0 in the board, create a new state with the players value in that position
        if val == 0:
            tempState[i] = player
            states[i+1] = tempState

    return states

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