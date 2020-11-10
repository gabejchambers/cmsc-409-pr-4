from minisom import MiniSom
import numpy as np
import pandas as pd


def normalize(df):
    # df = (df - np.mean(df, axis=0)) / np.std(df, axis=0)
    np_array = df.values
    df = (df - np_array.min(axis=0)) / (np_array.max(axis=0) - np_array.min(axis=0))
    df = df.values
    return df
    # result = df.copy()
    # min_value = 0
    # for feature_name in df.columns:
    #     max_value = df[feature_name].max()
    #     result[feature_name] = (df[feature_name] - min_value) / (max_value - min_value)
    # return result.values


def runCluster(in_data):
    df_data = pd.DataFrame(in_data)
    norm_data = normalize(df_data)
    print(in_data)
    print(norm_data)
