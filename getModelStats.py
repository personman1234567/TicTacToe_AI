from minRiskClassifier import *
from modelHelpers import *
from logisticRegressionClassifier import *
from decisionTreeClassifier import *

def getMinRiskStats():
    minRiskModel = createMinRiskModel()

    X_train, X_test, y_train, y_test = getModelData()

    getModelConfusionMatrix(minRiskModel, X_test, y_test)
    getClassificationReport(minRiskModel, X_test, y_test)

def getLogRegStats():
    logRegModel = createLogisticRegressionModel()

    X_train, X_test, y_train, y_test = getModelData()

    getModelConfusionMatrix(logRegModel, X_test, y_test)
    getClassificationReport(logRegModel, X_test, y_test)

def getDecTreeStats():
    decTreeModel = createDecisionTreeModel()

    X_train, X_test, y_train, y_test = getModelData()

    getModelConfusionMatrix(decTreeModel, X_test, y_test)
    getClassificationReport(decTreeModel, X_test, y_test)


def getAllStats():
    getMinRiskStats()
    getLogRegStats()
    getDecTreeStats()

getAllStats()