import pandas as pd
import matplotlib.pyplot as plt

from fit2DF import fit2DF
from csv2array import csv2array


#podatki = fit2DF('Corralejo_Betancuria_Morro_Jable.fit')
senzor = csv2array('datalog.csv')
print(senzor)
