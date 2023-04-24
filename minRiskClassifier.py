import csv
from math import exp, pi, sqrt

import pandas as pd

# Split the dataset by class values, returns a dictionary
def separate_by_class(dataset):
    separated = dict()

    for i in range(len(dataset)):
        vector = dataset.iloc[i]
        class_value = dataset['class'].iloc[i]
        if (class_value not in separated):
            separated[class_value] = list()
        separated[class_value].append(vector)
    return separated

# Convert string column to float
def str_column_to_float(dataset, column):
    for row in dataset:
        row[column] = float(row[column].strip())

def calculate_probability(x, mean, stdev):
    exponenet = exp(-((x-mean)**2 / (2 * stdev**2 )))
    return (1 / (sqrt(2 * pi) * stdev)) * exponenet

# Calculate the mean, stdev and count for each column in a dataset
# def summarize_dataset(dataset):

    # summaries = [(mean(column), stdev(column), len(column)) for column in zip(*dataset)]
    # del(summaries[-1])
    # return summaries

def summarize_by_class(dataset):
    grouped = dataset.groupby(dataset['class'])
    positiveData = grouped.get_group('positive')
    negativeData = grouped.get_group('negative')
    # separated = separate_by_class(dataset)
    summaries = dict()
    # for class_value, rows in separated.items():
    #     summaries[class_value] = summarize_dataset(rows)
    return summaries

# Calculate the probabilities of predicting each class for a given row
def calculate_class_probabilities(summaries, row):
    total_rows = sum([summaries[label][0][2] for label in summaries])
    probabilities = dict()
    for class_value, class_summaries in summaries.items():
        probabilities[class_value] = summaries[class_value][0][2]/float(total_rows)
        for i in range(len(class_summaries)):
            mean, stdev, count = class_summaries[i]
            probabilities[class_value] *= calculate_probability(row[i], mean, stdev)
    return probabilities

def main():
	# with open("data.csv", 'r') as file:
	# 	csvreader = csv.reader(file)
	# 	for row in csvreader:
	# 		print(row)

    data = pd.read_csv("dataNums.csv")

    grouped = data.groupby(data['class'])
    positiveData = grouped.get_group('positive')
    negativeData = grouped.get_group('negative')

    print(positiveData)

    positiveMeans = positiveData.mean(axis = 0, numeric_only=True)
    positiveStDevs = positiveData.std(numeric_only=True)

    negativeMeans = negativeData.mean(axis = 0, numeric_only=True)
    negativeStDevs = negativeData.std(numeric_only=True)

    summaries = dict()

    # print("Class: Positive")
    print(positiveMeans)
    print(positiveMeans['1'])
    # print(positiveStDevs)

    posSummaries = list()
    negSummaries = list()
    for i in range(1, 10):
        posSummaries.append((positiveMeans[str(i)], positiveStDevs[str(i)], len(positiveData)))
        negSummaries.append((negativeMeans[str(i)], negativeStDevs[str(i)], len(negativeData)))
    summaries['positive'] = posSummaries
    summaries['negative'] = negSummaries

    print(summaries['positive'])
    print(summaries['negative'])

    probabilities = calculate_class_probabilities(summaries, [1,1,1,1,-1,-1,1,-1,-1])

    print(probabilities)

    # print("Class: Negative")
    # print(negativeMeans)
    # print(negativeStDevs)

    # print(negativeData.std(numeric_only=True)['9'])


main()