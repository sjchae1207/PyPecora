import numpy as np
import scipy.io as sio
from scipy.spatial import distance

def PecoraDiff(x,y,E,epsilon):
    L=len(x)
    # print(L)
    X=np.zeros((L-E+1,E))
    Y=np.zeros((L-E+1,E))
    # print(X.shape)
    for e in range(E): 
        X[:,e]=x[e:L-E+e+1]
        Y[:,e]=y[e:L-E+e+1]
    dist_X=distance.squareform(distance.pdist(X))
    dist_Y=distance.squareform(distance.pdist(Y))
    # print(dist_X[0:5,0:5])
    r2_list=np.zeros((L-E+1,1))
    p_list=np.zeros((L-E+1,1))
    # for dot_i in range(L-E+1):
    for dot_i in range(L-E+1):
        print(dot_i)
        neighbors_x=np.argsort(dist_X[:,dot_i])
        diff_ratio=100
        num_neighbors=L-E+1
        sig_x=np.std(dist_X[:,dot_i],ddof=1)
        sig_y=np.std(dist_Y[:,dot_i],ddof=1)
        epsilon_s=epsilon*sig_y/sig_x
        
        while (diff_ratio>epsilon_s) and (num_neighbors>(E+1)):
            num_neighbors=num_neighbors-1
            nnx=neighbors_x[1:num_neighbors+1]
            temp_X=X[nnx,:]-X[dot_i,:]
            temp_Y=Y[nnx,:]-Y[dot_i,:]
            # print(num_neighbors)
            # print(temp_X[0])
            A=np.linalg.pinv(np.matmul(np.transpose(temp_X),temp_X))
            A=np.matmul(np.matmul(A,np.transpose(temp_X)),temp_Y) # edit required to be more simpler form
            diff_ratio_list=np.linalg.norm(temp_Y-temp_X.dot(A),axis=1)/np.linalg.norm(temp_X,axis=1)
            diff_ratio = max(diff_ratio_list)
        # print(num_neighbors)
        if num_neighbors == E:
            r2_list[dot_i]=0
        else:
            temp_mat=np.transpose(temp_X)@temp_Y@np.linalg.pinv(np.dot(np.transpose(temp_Y),temp_Y))@np.transpose(temp_Y)@temp_X@np.linalg.pinv(np.transpose(temp_X)@temp_X)
            temp_r2=np.trace(temp_mat)/num_neighbors
            r2_list[dot_i]=temp_r2
            # print(temp_r2)

        p_list[dot_i]=np.exp(-0.5*(num_neighbors-E-1)**2*temp_r2*E)


    return r2_list, p_list