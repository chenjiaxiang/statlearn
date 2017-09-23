import os
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
os.chdir('C:\Users\Administrator\Desktop\course\statlearn\experiment')

a=np.loadtxt('bezdekIris.data',dtype=float,delimiter=',',usecols=(0,1,2,3))
# print(a[:,0])
plt.style.use("ggplot")
plt.rcParams['axes.unicode_minus'] = False
plt.rcParams['font.sans-serif']=['SimHei'] 

df=pd.DataFrame()
df['sepal_length']=a[:,0]
df['sepal_width']=a[:,1]
df['petal_length']=a[:,2]
df['petal_width']=a[:,3]
df.boxplot()
plt.show()
