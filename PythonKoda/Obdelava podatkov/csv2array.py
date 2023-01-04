import pandas as pd

def csv2array(iCSVName):
    df = pd.read_csv(iCSVName)

    return(df)