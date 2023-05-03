# Helpful Links
    # https://machinelearningmastery.com/naive-bayes-classifier-scratch-python/
    # https://scikit-learn.org/stable/modules/naive_bayes.html#gaussian-naive-bayes

import csv
import copy
from math import exp, pi, sqrt
import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.naive_bayes import GaussianNB

def calculateProbability(x, mean, stdev):
    exponenet = exp(-((x-mean)**2 / (2 * stdev**2 )))
    return (1 / (sqrt(2 * pi) * stdev)) * exponenet


# Calculate the probabilities of predicting each class for a given row
def calculateClassProbabilities(summaries, row):
    totalRows = sum([summaries[label][0][2] for label in summaries])
    probabilities = dict()
    for classValue, classSummaries in summaries.items():
        probabilities[classValue] = summaries[classValue][0][2]/float(totalRows)
        for i in range(len(classSummaries)):
            mean, stdev, count = classSummaries[i]
            probabilities[classValue] *= calculateProbability(row[i], mean, stdev)
    return probabilities

def getSummaries(posData, negData):
    positiveMeans = posData.mean(axis = 0, numeric_only=True)
    positiveStDevs = posData.std(numeric_only=True)
    negativeMeans = negData.mean(axis = 0, numeric_only=True)
    negativeStDevs = negData.std(numeric_only=True)

    summaries = dict()

    posSummaries = list()
    negSummaries = list()
    for i in range(1, 10):
        posSummaries.append((positiveMeans[str(i)], positiveStDevs[str(i)], len(posData)))
        negSummaries.append((negativeMeans[str(i)], negativeStDevs[str(i)], len(negData)))
    summaries['positive'] = posSummaries
    summaries['negative'] = negSummaries

    return summaries

# Finds the minimum risk probabilities based on the board state
def minRiskClassifier(state):

    data = pd.read_csv("dataNums.csv")

    # Separate Date by Class
    grouped = data.groupby(data['class'])
    positiveData = grouped.get_group('positive')
    negativeData = grouped.get_group('negative')

    summaries = getSummaries(positiveData, negativeData)

    probabilities = calculateClassProbabilities(summaries, state)

    return probabilities


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

# Find the next best move and it's corresponding probability
def getNextBestMoveMinRisk(state, player):
    nextStates = getNextBoardStates(state, player)

    highestProbability = (0,0)
    for key, value in nextStates.items():
        probabilities = minRiskClassifier(value)
        if player == 1:
            if probabilities['positive'] > highestProbability[1]:
                highestProbability = (key, probabilities['positive'])
        else:
            if probabilities['negative'] > highestProbability[1]:
                highestProbability = (key, probabilities['negative'])

    return highestProbability

def minRiskClassifier(state, player):

    data = pd.read_csv("dataNums.csv")  

    X = data.drop("class", axis=1)
    y = data["class"]

    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.3, random_state=42)


    gnb = GaussianNB().fit(X_train, y_train)

    # Evalute the model
    # y_pred = gnb.predict(X_test)
    # accuracy = accuracy_score(y_test, y_pred)
    # print("Accuracy:", accuracy)

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
        probabilities = gnb.predict_proba(stateDF)

        if player == 1:
            if probabilities[0][0] > highestProbability[1]:
                highestProbability = (key, probabilities[0][0])
        else:
            if probabilities[0][1] > highestProbability[1]:
                highestProbability = (key, probabilities[0][1])

    return highestProbability



# ************ Testing ******************

# probabilities = minRiskClassifier([1,1,1,1,-1,-1,1,-1,-1])
# print(probabilities)

# states = getNextBoardStates([0,1,1,1,0,-1,1,-1,0], 1)
# print(states)

# nextMove = getNextBestMove([0,0,0,-1,1,0,0,0,0], 1)
# print(nextMove)