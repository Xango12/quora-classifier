import numpy as np
import re


def extract(filename):
    """
    Basic pre-processing logic to load dataset information.
    """
    input_file = open(filename)
    traindata = input_file.readlines()
    features = []
    targets = []

    for line in traindata:
        formatted_line = line.strip("\n")
        target_i = formatted_line.split(" ")[1]
        feature_i = re.sub(r"(\d+):", "", formatted_line).split(" ")[2:]

        targets.append(target_i)
        features.append(feature_i)

    matrix_features = np.array(features).astype(np.float)
    vector_targets = np.array(targets).astype(np.int)

    input_file.close()

    return matrix_features, vector_targets