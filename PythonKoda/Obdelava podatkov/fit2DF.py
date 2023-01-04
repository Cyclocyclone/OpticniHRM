from fitparse import FitFile
import pandas as pd


def fit2DF(iFName):
    fitfile = FitFile(iFName)

    while True:
        try:
            fitfile.messages
            break
        except KeyError:
            continue
    workout = []
    for record in fitfile.get_messages('record'):
        r = {}
        for record_data in record:
            r[record_data.name] = record_data.value
        workout.append(r)
    df = pd.DataFrame(workout)
    return df




