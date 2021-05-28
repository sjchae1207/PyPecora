import multiprocessing as mp
import numpy as np
from itertools import product
from os.path import dirname, join as pjoin
import scipy.io as sio
import time
def f(x,y,z,w):
    return np.array([x,y, z,w,x+y])

def g(x,y):
    a=range(3)
    b=np.arange(0,3)
    mat_fname = pjoin('experimental_data','HK_data')

    mat_contents=sio.loadmat(mat_fname)
    sorted(mat_contents.keys())
    #print(mat_contents)
    data=mat_contents['data'][:,0:8]
    # z[x,y]=x+y
    pool=mp.Pool(processes=8)
    result=pool.starmap(f, product(a,b,a,b))
    pool.close()
    pool.join()
    return result

A=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
# data_pairs = [ [3,5], [4,3], [7,3], [1,6] ]


z=np.empty((3,4))

if __name__=='__main__':
    t=time.time()
    z=np.array(g(1,2))
    print(z[:,0])
    
    # result
    # print(result)
    # print(np.reshape(result, (3,4)))
    print(time.time()-t)