

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import csv

x = []
y = []

with open('Data.csv','r') as csvfile:
    plot = csv.reader(csvfile, delimiter=',')
    headers = next(plot)

    for row in plot:
        x.append(row[0])
        y.append(int(row[2]))

plt.bar(x,y, color='g', width=0.72, label='Age')
plt.xlabel('Nombre')
plt.ylabel('Edad')
plt.title('Ejemplo')
plt.legend()
plt.show()