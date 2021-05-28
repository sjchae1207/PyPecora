import numpy as np
import scipy.io as sio
from scipy.spatial import distance
import multiprocessing as mp
from functools import partial

# multiprocessing module을 이용해서 병렬컴퓨팅하는 코드입니다
def PecoraDiff_per_dot(X,Y,E,epsilon,dot_ind):
    L=X.shape[0]
    dist_X=distance.squareform(distance.pdist(X))
    dist_Y=distance.squareform(distance.pdist(Y))
    neighbors_x=np.argsort(dist_X[:,dot_ind])
    diff_ratio=100
    num_neighbors=L-E+1
    sig_x=np.std(dist_X[:,dot_ind],ddof=1)
    sig_y=np.std(dist_Y[:,dot_ind],ddof=1)
    epsilon_s=epsilon*sig_y/sig_x
    print(dot_ind)
    while (diff_ratio>epsilon_s) and (num_neighbors>(E+1)):
        num_neighbors=num_neighbors-1
        nnx=neighbors_x[1:num_neighbors+1]
        temp_X=X[nnx,:]-X[dot_ind,:]
        temp_Y=Y[nnx,:]-Y[dot_ind,:]
        # edit required to be more simpler form
        A=np.linalg.pinv(np.matmul(np.transpose(temp_X),temp_X))
        A=np.matmul(np.matmul(A,np.transpose(temp_X)),temp_Y) 
        diff_ratio_list=np.linalg.norm(temp_Y-temp_X.dot(A),axis=1)/np.linalg.norm(temp_X,axis=1)
        diff_ratio = max(diff_ratio_list)
    # print(num_neighbors)
    if num_neighbors == E:
        r2=0
        p=1
    else:
        temp_mat=np.transpose(temp_X)@temp_Y@np.linalg.pinv(np.dot(np.transpose(temp_Y),temp_Y))@np.transpose(temp_Y)@temp_X@np.linalg.pinv(np.transpose(temp_X)@temp_X)
        r2=np.trace(temp_mat)/num_neighbors
        p=np.exp(-0.5*(num_neighbors-E-1)**2*r2*E)
    return [r2, p]

def PecoraDiff(x,y,E,epsilon):
    L=len(x)
    # print(L)
    X=np.zeros((L-E+1,E))
    Y=np.zeros((L-E+1,E))
    # print(X.shape)
    for e in range(E): 
        X[:,e]=x[e:L-E+e+1]
        Y[:,e]=y[e:L-E+e+1]

    # 여기서 병렬 컴퓨팅을 해서 80가지 dot_ind에 대해 동시에 계산하려고 했습니다
    # 제 데스크탑에서는 이 부분을 사용했을 때 병렬 컴퓨팅이 되는 것을 확인했습니다.
    pool=mp.Pool(processes=80)
    result=pool.map(partial(PecoraDiff_per_dot, X, Y, E, epsilon), range(L-E+1))
    pool.close()
    pool.join()
          
    result_array=np.array(result)
    r2_list=result_array[:,0]
    p_list=result_array[:,1]

    return r2_list, p_list