
import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import pandas as pd
import csv
from datetime import datetime


df = pd.read_csv('Data_lab.csv')

dates = df['AAPL_x']

x=[datetime.strptime(date, "%Y-%m-%d").date() for date in dates]
floats = df['AAPL_y']

fig,(ax1,ax2) = plt.subplots(2,1)

ax1.plot(x, color='red')
ax2.plot(floats,color='blue')
ax1.set_title('AAPL-x')
ax2.set_title('AAPL-y')

fig.tight_layout()
plt.show()
