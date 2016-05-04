import numpy as np
from numpy import linalg
import math
iter_num=10000

def matrixNorm(mat,r,c):
    #maxMat=sumABS(mat,0,c)
    maxMat=mat[0][0]
    for i in range(1,r):
        temp=mat[i][i]
        if(maxMat<temp):
            maxMat=temp
    return maxMat
def sumABS(mat,currentR,col):
    sumRow=0
    for i in range(col):
        sumRow=sumRow+abs(mat[currentR][i])
    return sumRow
def normalVect(v,size):
    for i in range(size):
        v[i]=math.ceil(v[i]*100000)/100000
    return v

def matrixDiagonal(matrix,NumRow,NumCol):
    #TO CHECK
    mat=[]
    for r in range(NumRow):
        row=[]
        for c in range (NumCol):
            if(c==r):
                row.append(matrix[r][c])
            else:
                row.append(0)
        mat.append(row)
    return mat
def matrixLow(matrix,NumRow,NumCol):
    #TO CHECK
    mat=[]
    for r in range(NumRow):
        row=[]
        for c in range (NumCol):
            if(c<r):                
                row.append(matrix[r][c])            
            else:
                row.append(0)
        mat.append(row)
    return mat
def matrixUp(matrix,NumRow,NumCol):
    #TO Check
    mat=[]
    for r in range(NumRow):
        row=[]
        for c in range (NumCol):
            if(c>r):                
                row.append(matrix[r][c])            
            else:
                row.append(0)
        mat.append(row)
    return mat
def VectorZero(size):
    vector=[0 for __ in range(size)]
    return vector
def addD2L(D,L,NumRow,NumCol):
    mat=()
    for r in range(NumRow):
        row=()
        for c in range (NumCol):
            if(c<r):                
                row=row+(L[r][c],)
            if(c==r):
                row=row+(D[r][c],)
            if(c>r):
                row=row+(0,)
        mat=mat+(row,)
    return mat


def normalMatrix(metrix,NumRow,NumCol ):
    for r in range (NumRow):
        for c in range (NumCol):
            metrix[r][c]=int(metrix[r][c]%256)
    return metrix
def VectorSubstruction(vectorA,vectorB,size):
    #return A-B
    vectorAns=[]
    for i in range(size):
        vectorAns.append(vectorA[i]-vectorB[i])
    return vectorAns
    
def DominantDiagonal(matrix,row,col): 
    #check Date:15.03.2016
    for r in range(row):
        sumRow=0
        for c in range(col):
            if(r!=c):
                sumRow=sumRow+abs(matrix[r][c])
        if(abs(matrix[r][r])<=sumRow):
            return False
    return True

def GnS(matrix,row,col,vectorb,sizeV,LeftMatrix,G,U):
    xPre=VectorZero(sizeV)  
    G_1=G
    for __ in range (iter_num): #to change to error size    
        RightVector=VectorSubstruction(vectorb,np.dot(U,xPre),sizeV)
        xCurrent=normalVect(np.dot(LeftMatrix,RightVector),sizeV)
        G=mulMat(G,row,col,G_1,row,col)
        if(matrixNorm(G,row,col)<1e-100):
            return list(xCurrent)
        xPre=xCurrent
    return xCurrent
def mulMat(matrix1,r1,c1,matrix2,r2,c2):
    ans=[]
    if(c1!=r2):
        return None
    for r in range(r1):
        vRow=[]
        for i in range(c2):
            var=0
            for c in range(c1):
                var=var+matrix1[r][c]*matrix2[c][i]
            vRow.append(var)
        ans.append(vRow)
    return ans

def test():
    row1,col1=4,4

    matrix1=[[0.54236,0,0,0],
                        [0,0.53153,0,0],
                        [0,0, 0.47003,0],
                        [0,0,0,0.52342]]
    matrix2=[[68,55,66,87],
                        [55,43,56,78],
                        [51,39,52,75],
                        [56,43,56,78]]
    matrix3=[[ 36.88048 , 29.8298 ,  35.79576  ,47.18532],
                             [ 29.23415,  22.85579  ,29.76568,  41.45934],
                             [ 23.97153 , 18.33117 , 24.44156 , 35.25225],
                             [ 29.31152,  22.50706  ,29.31152  ,40.82676]]
    matrix3=(np.array(matrix3)).transpose()
    D=matrixDiagonal(matrix1, row1,col1)
    L=matrixLow(matrix1, row1,col1)
    U=matrixUp(matrix1, row1,col1)
    #(L+D)^-1
    LeftMatrix=linalg.inv(addD2L(D,L, row1,col1))
    
    G=mulMat(LeftMatrix,row1,col1,np.array(U),row1,col1)
    matrix4=[]
    matrix5=[]
    for r in range(row1):
        vectorBefore=matrix2[r] #should be printed after
        vectorBefore=np.dot(matrix1,vectorBefore)
        vector=matrix3[r]
        matrix4.append(GnS(matrix1,row1,col1, vector, row1,LeftMatrix,G,U))
        matrix5.append(GnS(matrix1,row1,col1, vectorBefore, row1,LeftMatrix,G,U))
    print(np.array(matrix4))
    print(np.array(matrix5))
#test()

#[[ 68.       56.12064  76.15634  90.14811]
 #[ 53.90175  43.       63.3272   79.20856]
 #[ 44.19856  34.48756  52.       67.34984]
 #[ 54.0444   42.34392  62.36096  78.     ]]

