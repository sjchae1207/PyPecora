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
from itertools import product

def HK_pecora_E7( effect_ind,cause_ind, temp_ind):
    mat_fname = pjoin('experimental_data','HK_data')
    mat_contents=sio.loadmat(mat_fname)
    sorted(mat_contents.keys())
    #print(mat_contents)
    data=mat_contents['data'][:,0:8]
    temp_eps=temp_ind/100+0.01  
    print(effect_ind,cause_ind, temp_eps)
    [r2_list, p_list]=PecoraDiff(data[:,cause_ind],data[:,effect_ind],7,temp_eps)

    return effect_ind, cause_ind, temp_eps, np.mean(r2_list), np.mean(p_list)

#data_dir = pjoin(dirname(sio.__file__),'matlab','test','data')
#print(data_dir)
# mat_fname = pjoin('experimental_data','HK_data')
# print(mat_fname)

t=time.time()
# mat_contents=sio.loadmat(mat_fname)
# sorted(mat_contents.keys())
# #print(mat_contents)
# data=mat_contents['data'][:,0:8]

# cause_inds=range(8)
# effect_inds=range(8)
# eps_inds=range(100)
cause_inds=[0]
effect_inds=[1]
eps_inds=[5]
if __name__=='__main__':
    pool=mp.Pool()
    result=pool.starmap(HK_pecora_E7, product(cause_inds,effect_inds,eps_inds))
    pool.close()
    pool.join()

    # print(np.reshape(result, (3,4)))
print(time.time()-t)
mat_file=mdic={"hk_pecora_E7":result}
sio.savemat("hk_pecora_E7.mat",mat_file)