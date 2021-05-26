from os.path import dirname, join as pjoin
from numpy.core.fromnumeric import trace
from numpy.lib.shape_base import expand_dims
import pandas as pd
import numpy as np
import scipy.io as sio
from scipy.spatial import distance



def PecoraDiff(x,y,E,epsilon):
    L=len(x)
    print(L)
    X=np.zeros((L-E+1,E))
    Y=np.zeros((L-E+1,E))
    print(X.shape)
    for e in range(E): 
        X[:,e]=x[e:L-E+e+1]
        Y[:,e]=y[e:L-E+e+1]
    dist_X=distance.squareform(distance.pdist(X))
    dist_Y=distance.squareform(distance.pdist(Y))
    print(dist_X.shape)
    r2_list=np.zeros((L-E+1,1))
    p_list=np.zeros((L-E+1,1))
    for dot_i in range(1):
        neighbors_x=np.argsort(dist_X[:,dot_i])
        diff_ratio=100
        num_neighbors=L-E+1
        sig_x=np.std(dist_X[:,dot_i])
        sig_y=np.std(dist_Y[:,dot_i])
        epsilon_s=epsilon*sig_y/sig_x

        while (diff_ratio>epsilon_s) and (num_neighbors>4):
            num_neighbors=num_neighbors-1
            nnx=neighbors_x[3:num_neighbors+1]
            temp_X=X[nnx,:]-X[dot_i,:]
            temp_Y=Y[nnx,:]-Y[dot_i,:]
            A=np.linalg.pinv(np.matmul(np.transpose(temp_X),temp_X))
            A=np.matmul(np.matmul(A,np.transpose(temp_X)),temp_Y) # edit required to be more simpler form

            diff_ratio_list=np.linalg.norm(temp_Y-temp_X.dot(A),axis=1)

            diff_ratio = max(diff_ratio_list)
        if num_neighbors == 3:
            r2_list[dot_i]=0
        else:
            temp_mat=np.transpose(temp_X)@temp_Y@np.linalg.pinv(np.dot(np.transpose(temp_Y),temp_Y))@np.transpose(temp_Y)@temp_X@np.linalg.pinv(np.transpose(temp_X)@temp_X)
            temp_r2=np.trace(temp_mat)/num_neighbors
            r2_list[dot_i]=temp_r2
        

        p_list[dot_i]=np.exp(-0.5*(num_neighbors-E-1)**2*temp_r2*E)


    return r2_list, p_list

#data_dir = pjoin(dirname(sio.__file__),'matlab','test','data')
#print(data_dir)
mat_fname = pjoin('PyPecora','experimental_data','HK_data')
print(mat_fname)


mat_contents=sio.loadmat(mat_fname)
sorted(mat_contents.keys())
#print(mat_contents)
data=mat_contents['data'][:,0:8]
print(data)
x=data[:,0]
y=data[:,1]
#print(x)
print(distance.squareform(distance.pdist(data)))

print(PecoraDiff(x,y,7,0.01))

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
