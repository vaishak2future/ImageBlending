'''
  File name: getSolutionVect.py
  Author: Vaishak Kumar, Cathleen Gui 
  Date created:
'''

'''
Function computes solution vector b in the system Ax = b.
(INPUT) indexes: h'×w' matrix representing the indices of each replacement pixel.
(INPUT) source: h×w matrix representing one color channel of the source image.
(INPUT) target: h'×w' matrix representing one color channel of target image. 
(INPUT) offsetX: The x-axis offset of the source image with respect to the target image.
(INPUT) offsetY: The y-axis offset of the source image with respect to the target image.
(OUTPUT) solVectorb: 1×N vector representing the solution vector.  
'''
import numpy as np
from scipy import signal

def getSolutionVect(indexes, source, target, offsetX, offsetY):
  #Offset values for boundary additions
  direction = np.asarray([[-1,0],[0,-1],[0,1],[1,0]])
  #Laplace filter values
  laplace = np.asarray([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
  sourceLaplace = signal.convolve(source,laplace,'same')
  
  b = np.empty(np.count_nonzero(indexes)) # Vector of pixels from source Laplace
  
  N = b.shape[0]
  boundaryAdditions = np.zeros((N,4), dtype = "float64")
  
  for i in range(indexes.shape[0]):
    for j in range(indexes.shape[1]):
      if indexes[i][j] != 0:
        #Populate b with source Laplacian values for pixels to be blended  
        b[indexes[i][j]-1] = sourceLaplace[i-offsetY,j-offsetX]
        #Check if neighbors are in target and add them to boundary additions
        for a in range(4):
          ii = i+direction[a,0]
          jj = j+direction[a,1]
          if indexes[ii,jj] == 0:
              boundaryAdditions[indexes[i][j]-1,a] = target[ii,jj]
              
  SolVectorb = b +boundaryAdditions[:,0] + boundaryAdditions[:,1] + boundaryAdditions[:,2] + boundaryAdditions[:,3]
  return SolVectorb
