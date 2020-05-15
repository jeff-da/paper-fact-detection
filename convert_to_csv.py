import csv
import ast
import numpy as np

writer = csv.DictWriter(open("results_human.csv", 'w'), fieldnames=["token","score"])
writer.writeheader()

def softmax(x):
    """Compute softmax values for each sets of scores in x."""
    e_x = np.exp(x - np.max(x))
    return e_x / e_x.sum(axis=0) # only difference

for line in open('test_predictions_source.txt'):
    if len(line) > 5:
        line = line.rstrip()
        token = line.split()[0]
        values = ast.literal_eval(line.split()[2] + line.split()[3])
        values = softmax(values)
        writer.writerow({"token": token, "score": values[1]})

writer = csv.DictWriter(open("results_generated.csv", 'w'), fieldnames=["token","score"])
writer.writeheader()

max_score = 0
for line in open('test_predictions.txt'):
    if len(line) > 5:
        line = line.rstrip()
        token = line.split()[0]
        values = ast.literal_eval(line.split()[2] + line.split()[3])
        values = softmax(values)
        max_score = max(max_score, values[1])

for line in open('test_predictions.txt'):
    if len(line) > 5:
        line = line.rstrip()
        token = line.split()[0]
        values = ast.literal_eval(line.split()[2] + line.split()[3])
        values = softmax(values)
        writer.writerow({"token": token, "score": values[1] / max_score})

