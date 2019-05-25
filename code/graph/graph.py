from matplotlib import pyplot as plt
import pandas as pd
import numpy as np

def plotXyScatter(df, title):
    plot(df, title, 'scatter')
   
def plotLine(df, title):
    plot(df, title, 'line') 
    
def plot(df, title, kind):
    columns = list(df.columns.values)
    
    if len(columns) < 2:
        print('Not enough columns')
        return
    
    fig, ax = plt.subplots()
    for y in columns[1:]:
        df.plot(kind=kind, x=columns[0], y=y, label=y, ax=ax)
    
    ax.legend()
    plt.title(title)
    
def show():
    plt.show()
