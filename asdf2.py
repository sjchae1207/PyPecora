import multiprocessing as mp
import numpy as np
from itertools import product
from os.path import dirname, join as pjoin
import scipy.io as sio

def f(x,y):
    mat_fname = pjoin('experimental_data','HK_data')

    mat_contents=sio.loadmat(mat_fname)
    sorted(mat_contents.keys())
    #print(mat_contents)
    data=mat_contents['data'][:,0:8]
    # z[x,y]=x+y
    return x+y, data[0,2]

A=[[1,2,3],[4,5,6],[7,8,9],[10,11,12]]
# data_pairs = [ [3,5], [4,3], [7,3], [1,6] ]
x=range(3)
y=np.arange(0,8,2)

z=np.empty((3,4))

if __name__=='__main__':
    pool=mp.Pool(processes=8)
    result=pool.starmap(f, product(x,y))
    pool.close()
    pool.join()
    result
    print(result)
    # print(np.reshape(result, (3,4)))