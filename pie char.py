import matplotlib as plt
import numpy as np

y=np.array ([35,25,25,15])
mylabels=['Apples','Bananas','Charries','Dates']
myexplode=[0.2,0,0,0]

plt.pie(y,labels=mylebels,explode=myexplode,shadow=True)