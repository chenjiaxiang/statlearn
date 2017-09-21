import numpy as np
import scipy
from scipy.optimize import minimize

def func(x,sign=1.0):
	return sign*(10-x[0]**2-x[1]**2)

def func_deriv(x,sign=1.0):
	deriv_1 = sign * (-2*x[0])
	deriv_2 = sign * (-2*x[1])
	return np.array([deriv_1,deriv_2]) 

cons = ({'type':'eq',
		 'fun':lambda x:np.array([x[0]+x[1]]),
		 'jac':lambda x:np.array([1.0,1.0])},
		{'type':'ineq',
		 'fun':lambda x:np.array([-(x[0]**2)+x[1]]),
		 'jac':lambda x:np.array([-2.0*x[0],1.0])})

res = minimize(func,[-1.0,1.0],args=(1.0,),jac=func_deriv,constraints=cons,method='SLSQP',options={'disp':True})
print(res.x)
