'''
  File name: getCoefficientMatrix.py
  Author: Vaishak Kumar, Cathleen Gui
  Date created:
'''

'''
Function aids in computing the intensities of the replacement pixels by computing coefficient matrix A. 
(INPUT) indexes: h'×w' matrix representing the indices of each replacement pixel.
(OUTPUT) coeffA: an N×N sparse matrix representing the Coefﬁcient Matrix, where N is the number of replacement pixels.
'''

import numpy as np

def getCoefficientMatrix(indexes):
  #Offset values: Self, Up, Left, Right, Down
  direction = np.asarray([[0,0],[-1,0],[0,-1],[0,1],[1,0]])
  #count nonzero entries to find dimensions of coeffA and create NxN matrix of zeroes
  N = np.count_nonzero(indexes) 
  #print(N)
  coeffA = np.zeros((N,N), dtype = "int32")
  laplace = np.asarray([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])

  for i in range(indexes.shape[0]):
    for j in range(indexes.shape[1]):
      #Diagonals are middle value of the Laplacian
      #if i == j:
        #coeffA[i,j] = laplace[1,1]
      #For non-masked pixels, the corresponding row ai of coeffA gives the operations needed to compute th convolution on that pixel
      if indexes[i,j] != 0:
        for a in range(5):
          ii = i+direction[a,0]
          jj = j+direction[a,1]
          if indexes[ii,jj] != 0:
            coeffA[indexes[i,j]-1,indexes[ii,jj]-1] = laplace[1+direction[a,0],1+direction[a,1]]
  return coeffA

