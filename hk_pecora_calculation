from os.path import dirname, join as pjoin
#from numpy.core.fromnumeric import trace
#from numpy.lib.shape_base import expand_dims
# import pandas as pd
import numpy as np
import scipy.io as sio
from scipy.spatial import distance
import time
from Pecora import PecoraDiff
import multiprocessing as mp


#data_dir = pjoin(dirname(sio.__file__),'matlab','test','data')
#print(data_dir)
mat_fname = pjoin('experimental_data','HK_data')
print(mat_fname)

t=time.time()
mat_contents=sio.loadmat(mat_fname)
sorted(mat_contents.keys())
#print(mat_contents)
data=mat_contents['data'][:,0:8]


diff_measure_r2=np.empty((8,8,100))
diff_measure_r2[:]=np.nan
diff_measure_p=np.empty((8,8,100))
diff_measure_p[:]=np.nan

eps_list=np.arange(0,1,0.01)
for effect_ind in range(8):
    for cause_ind in range(8):
        for eps_ind in range(100):
            temp_eps=eps_ind/100;
            print(eps_ind)
            [r2_list, p_list]=PecoraDiff(data[:,cause_ind],data[:,effect_ind],7,temp_eps)
            diff_measure_r2[effect_ind, cause_ind, eps_ind]=np.mean(r2_list) 
            diff_measure_p[effect_ind, cause_ind,eps_ind]=1-np.mean(p_list)

# print(data)
# x=data[:,0]
# y=data[:,1]
#print(x)
#print(distance.squareform(distance.pdist(data)))

# print(PecoraDiff(x,y,7,0.01))

elapsed=time.time()-t
print(elapsed)
