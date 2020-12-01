import pandas as pd
import numpy as np
import os

def read_data():
    raw_data_path = os.path.join(os.path.pardir, 'data', 'raw')
    prima_path = os.path.join(raw_data_path, 'pima-data.csv')
    df = pd.read_csv(prima_path)
    return df

def process_data(df):
    del df['skin']
    diabetes_map = {True: 1, False: 0}
    df['diabetes'] = df['diabetes'].map(diabetes_map)
    return df

def write_data(df):
    processed_path = os.path.join(os.path.pardir, 'data', 'processed', 'pima-data-processed.csv')
    df.to_csv(processed_path)

if __name__ == '__main__':
    df = read_data()
    df = process_data(df)
    write_data(df)
