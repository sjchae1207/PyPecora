from os.path import dirname, join as pjoin
#from numpy.core.fromnumeric import trace
#from numpy.lib.shape_base import expand_dims
import pandas as pd
import numpy as np
import scipy.io as sio
from scipy.spatial import distance
import time
from Pecora import PecoraDiff


#data_dir = pjoin(dirname(sio.__file__),'matlab','test','data')
#print(data_dir)
mat_fname = pjoin('experimental_data','HK_data')
print(mat_fname)

t=time.time()
mat_contents=sio.loadmat(mat_fname)
sorted(mat_contents.keys())
#print(mat_contents)
data=mat_contents['data'][:,0:8]
# print(data)
x=data[:,0]
y=data[:,1]
#print(x)
#print(distance.squareform(distance.pdist(data)))

print(PecoraDiff(x,y,7,0.01))

elapsed=time.time()-t
print(elapsed)
"""
class Pecora():
    def __init__(self):
        self.r2=0
        self.p=1
    def differentiable_measure(self,x,y,E,epsilon):
        L=len(x)
        X=np.zeros(E,L-E+1)
        Y=np.array(E,L-E+1)
        for e in range(E): 
            X[:,e]=x[e:L-E+e+1]
            Y[:,e]=y[e:L-E+e+1]
        dist_X=distance.pdist(X,Y)
        dist_Y=distance.pdist(X,Y)

        return self.r2, self.p
"""
