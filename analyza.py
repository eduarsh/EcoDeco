import numpy as np
import math
from numpy import random
from numpy import linalg
import algebraMatrix as am
from dns.rdatatype import NULL
from numpy.core.defchararray import rstrip
def encrypt(encryptMatrix,rowEn,colEn,plainMatrix,rowPlainImage,colPlainImage):
    #Simple matrix vector multipication
    #4 EACH ROW
    #Date Check:14.03.2016
    encryptmat1=am.mulMat(encryptMatrix,rowEn,colEn,plainMatrix,rowPlainImage,colPlainImage)
    encryptmat1=(np.array(encryptmat1)).transpose()
    encryptmat2=am.mulMat(encryptMatrix,rowEn,colEn,encryptmat1,rowPlainImage,colPlainImage)
    encryptmat2=(np.array(encryptmat2)).transpose()
    encryptmat3=am.mulMat(encryptMatrix,rowEn,colEn,encryptmat2,rowPlainImage,colPlainImage)
    #????????????????????????????????????/// 
 #for r in range(rowPlainImage):
        #image vector is row vector
        #imageRowVector=plainMatrix[r]
        #encryptmat.append(am.multUMatVec(encryptMatrix,rowEn,colEn,imageRowVector))
    matrix_to_file('data/Encrypted.txt', encryptmat3, rowPlainImage, colPlainImage)
    matrix_to_file('data/EncryptedNormal.txt', am.normalMatrix(encryptmat3,rowPlainImage,colPlainImage), rowPlainImage, colPlainImage)
        
def decrypt(decryptMatrix,numRow,numCol,codeMatrix,rowCodeImage,colCodeImage):
    #Date Check: XXXXXXXXX 
    #4 EACH ROW
    # numerical iterative MatrixKey*image2find=encrypt
    # xCurrent== image2find
    # vectorb == encryptVector
    #x[r+1]=((D+L)^-1)*(b-Ux(r))
    def dec(decryptMatrix,numRow,numCol,codeMatrix,rowCodeImage,colCodeImage):
        codeMatrixTrans=(np.array(codeMatrix)).transpose()
        D=am.matrixDiagonal(decryptMatrix,rowCodeImage,colCodeImage)
        L=am.matrixLow(decryptMatrix,rowCodeImage,colCodeImage)
        U=am.matrixUp(decryptMatrix,rowCodeImage,colCodeImage)
        #(L+D)^-1
        LeftMatrix=linalg.inv(am.addD2L(D,L,numRow,numCol))
        G=am.mulMat(LeftMatrix, numRow,numCol, np.array(U), numRow,numCol)
        decryptmat=[]
        #for each  row 2DOOOOOOO
        for r in range(rowCodeImage): 
            xCurrent=am.GnS(decryptMatrix,numRow,numCol, codeMatrixTrans[r], colCodeImage,LeftMatrix,G,U)
            decryptmat.append(xCurrent)
        decryptmat=(np.array(decryptmat)).transpose()
        return decryptmat
    
    decryptmat1=dec(decryptMatrix,numRow,numCol,codeMatrix,rowCodeImage,colCodeImage)
    print(decryptmat1)
    decryptmat1=(np.array(decryptmat1)).transpose()
    decryptmat2=dec(decryptMatrix,numRow,numCol,decryptmat1,rowCodeImage,colCodeImage)
    print(decryptmat2)
    decryptmat2=(np.array(decryptmat2)).transpose()
    decryptmat3=dec(decryptMatrix,numRow,numCol,decryptmat2,rowCodeImage,colCodeImage)
    matrix_to_file('data/Decrypted.txt', decryptmat3, rowCodeImage, colCodeImage)
    matrix_to_file('data/DecryptedNormal.txt', am.normalMatrix(decryptmat3,rowCodeImage,colCodeImage), rowCodeImage, colCodeImage)

#MATRIX ACTION
def createEncryptMatrix(row,col,fileNameImage):
    #NOT POSIBBLE 2 WRITE BITS 2 FILE
    #Date check: 13.03.2016
    print("start createEncryptMatrix")
    matrix=[]
    #creating inversable Key Matrix
    for r in range(row):
        rowVec=[]
        for c in range(col):
            temp=0
            rowVec.append(temp)
        rowVec[r]=random.random()
        rowVec[r]=math.ceil(rowVec[r]*100000)/100000
        matrix.append(rowVec)           
    matrix_to_file(fileNameImage,matrix,row,col)
    #matrix=file_to_matrix(fileNameImage)
    #if(am.DominantDiagonal(matrix, rowNum,colNum)):
      #  return
    #createEncryptMatrix(rowNum,colNum,fileNameImage)
    print("end createEncryptMatrix,")
def file_to_matrix(fileNameKey):
    #Date check:13.03.2016
    contents=[]
    with open(fileNameKey,'r') as f:
        for line in f:
            line=line.rstrip('\n')
            line=map(float,line.split(','))
            contents.append(line)
    return contents
def matrix_to_file(fileName,matrix,row,col):
    #Date check:14.03.2016 
    file=open(fileName,'w')
    for r in range(row):
        for c in range(col):
            if(c==col-1):
                file.write("{0}".format(matrix[r][c]))
            else:
                file.write("{0},".format(matrix[r][c]))
        file.write("\n") 
        
#testcolPlainImage
#Matrix=[[1,0,1],[0,1,1],[0,0,1]]
#matrix_to_file('test.txt',Matrix,3,3)
#print(file_to_matrix('test.txt'))
#plainMatrix=[[254,50,17],[15,252,32],[44,552,66]]
#decrypt(encryptMatrix,3,3,plainMatrix,3,3)
#CodeMatrix=file_to_matrix('data/Decrypted.txt')
#encrypt(encryptMatrix, 3, 3, CodeMatrix, 3, 3)