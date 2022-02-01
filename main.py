import numpy as np
from matplotlib import pyplot as plt
from  matplotlib.ticker import MultipleLocator
import csv

x=[]
scores=[]
with open('daily_india.csv', 'r') as F:
    rF=csv.reader(F)
    for R in rF:
        for i in R:
            dig=int(str(i)[0])
            if dig!=0:
                x.append(dig)

for i in range(1,10):
    scores.append(x.count(i))


binbounds = np.linspace(1, 10, 10)
rwidth = 0.5
width = binbounds[1] - binbounds[0]
bars = plt.bar(binbounds[:-1], height=scores, width=width * rwidth, align='center')
plt.gca().xaxis.set_major_locator(MultipleLocator(1))
for rect in bars:
    x, y = rect.get_xy()
    w = rect.get_width()
    h = rect.get_height()
    plt.text(x + w / 2, h, f'{round(h/698,2)}\n', ha='center', va='center')
plt.show()