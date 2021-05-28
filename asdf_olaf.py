
import multiprocessing as mp
import numpy as np
from itertools import product
import time

def f(x,y):
    # z[x,y]=x+y
    return x+y, x

# time.sleep(10)
# data_pairs = [ [3,5], [4,3], [7,3], [1,6] ]

print('__name__')
if __name__=='__main__':
    x=range(1000)
    y=np.arange(0,8,1000)
    pool=mp.Pool(processes=2)
    print(mp.cpu_count())
    t=time.time()
    print(t)    
    result=pool.starmap(f, product(x,y))
    pool.close()
    pool.join()
    result
    print(result)
    # print(np.reshape(result, (3,4)))
    print(time.time()-t)