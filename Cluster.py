import numpy as np
import pandas as pd
from minisom import MiniSom


def normalize(df):
    np_array = df.values
    df = (df - np_array.min(axis=0)) / (np_array.max(axis=0) - np_array.min(axis=0))
    df = df.values
    return df


def runCluster(in_data):
    df_data = pd.DataFrame(in_data)
    norm_data = normalize(df_data)
    som_shape = (1, 100)
    som = MiniSom(som_shape[0], som_shape[1], norm_data.shape[1], sigma=.1, learning_rate=.5,
                  neighborhood_function='gaussian')
    som.train_batch(norm_data, 700, verbose=True)
    winner_coordinates = np.array([som.winner(x) for x in norm_data]).T
    winners = []
    for row in norm_data:
        winners.append(som.winner(row))
    print("# winners: " + str(len(set(winners))))

