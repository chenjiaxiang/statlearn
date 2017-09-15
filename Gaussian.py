import random
import numpy as np
n = [100,1000,10000,100000]
list = []
for i in xrange(len(n)):
	list.append(np.ones((n[i])))
	for k in xrange(n[i]):
		list[i][k]=random.gauss(2,3)
	print(list[i].mean(),list[i].var())




