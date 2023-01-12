import pandas as pd
import matplotlib.pyplot as plt
pd.options.plotting.backend = "plotly"
import plotly.express as px
import plotly as plotly
import os
import plotly.graph_objects as go

from fit2DF import fit2DF
from csv2array import csv2array

pd.set_option('display.max_rows', None)


podatki = fit2DF('trenazer040123.fit')
print(podatki)
senzor = csv2array('HRMLog040123.csv')
print(senzor)


podatkiZ = podatki.loc[:,['timestamp','heart_rate', 'power']]
#podatkiZ = podatki.loc[:,['timestamp','heart_rate']]
#podatkiZ['timestamp'] = podatkiZ['timestamp'].replace({'2023', '0000'}, regex=True)
#podatkiZ['timestamp'] = podatkiZ['timestamp'].str.replace()
podatkiZ['timestamp'] = podatkiZ['timestamp'].dt.time
print(podatkiZ)


fig = go.Figure()

fig.add_trace(go.Scatter(x=senzor.Cas, y=senzor.HR, name="OHRM"))
fig.add_trace(go.Scatter(x=podatkiZ.timestamp, y=podatkiZ.heart_rate, name="Pas"))
fig.add_trace(go.Scatter(x=podatkiZ.timestamp, y=podatkiZ.power, name="Moc"))

fig.update_layout(title_text="Senzor in pas na roki")

#fig.show()

if not os.path.exists("images"):
    os.mkdir("images")

fig.write_image("images/Trenazer.pdf")


plotly.offline.plot(fig)

