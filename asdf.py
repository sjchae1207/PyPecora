import multiprocessing as mp
import numpy as np
from itertools import product
import time
import scipy.io as sio
def f(x,y):
    # z[x,y]=x+y
    return x+y, x

t=time.time()
# data_pairs = [ [3,5], [4,3], [7,3], [1,6] ]
x=range(5)
y=np.arange(0,8,2)

z=np.empty((3,4))

if __name__=='__main__':
    pool=mp.Pool(processes=8)
    print(mp.cpu_count())
    result=pool.starmap(f, product(x,y))
    pool.close()
    pool.join()
    result
    print(result)
    mdic={"b":result}
    sio.savemat("b.mat",mdic)
    # print(np.reshape(result, (3,4)))
print(time.time()-t)