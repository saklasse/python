import pandas as pd

def openFile(name):
    df=pd.read_csv(name, sep=',')
    return df
