# Helpful Links
    # https://machinelearningmastery.com/naive-bayes-classifier-scratch-python/

import csv
import copy
from math import exp, pi, sqrt
import pandas as pd

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
            states[i] = tempState

    return states

# Find the next best move and it's corresponding probability
def getNextBestMove(state, player):
    nextStates = getNextBoardStates(state, player)

    highestProbability = (0,0)
    for key, value in nextStates.items():
        probabilities = minRiskClassifier(value)
        if probabilities['positive'] > highestProbability[1]:
            highestProbability = (key, probabilities['positive'])

    return highestProbability


# ************ Testing ******************

# probabilities = minRiskClassifier([1,1,1,1,-1,-1,1,-1,-1])
# print(probabilities)

# states = getNextBoardStates([0,1,1,1,0,-1,1,-1,0], 1)
# print(states)

nextMove = getNextBestMove([0,0,0,-1,1,0,0,0,0], 1)
print(nextMove)