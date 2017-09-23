import os
import numpy as np
import numpy.linalg
os.chdir('C:\Users\Administrator\Desktop\course\statlearn\experiment')

a=np.loadtxt('bezdekIris.data',dtype=float,delimiter=',',usecols=(0,1,2,3))
cov=np.cov(a.T)
corr=np.corrcoef(a.T)
evalue,evector=np.linalg.eig(cov)
print evalue,evector
# print numpy.linalg.norm(evector[:,1])
print np.dot(a,evector)
