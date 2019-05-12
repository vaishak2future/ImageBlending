'''
  File name: seamlessCloningPoisson.py
  Author: Vaishak Kumar, Cathleen Gui
  Date created:
'''

'''
Wrapper function.
(INPUT) sourceImg: h×w×3 matrix representing the source image.
(INPUT) targetImg: h0×w0×3 matrix representing the target image.
(INPUT) mask: The logical matrix h×w representing the replacement region.
(INPUT) offsetX: The x-axis offset of the source image with respect to the target image.
(INPUT) offsetY: The y-axis offset of the source image with respect to the target image.
(OUTPUT) resultImg: h0×w0×3 matrix representing the resulting cloned image.   
'''
import numpy as np
from PIL import Image
from getIndexes import getIndexes
from getCoefficientMatrix import getCoefficientMatrix
from getSolutionVect import getSolutionVect
from reconstructImg import reconstructImg
import matplotlib.pyplot as plt

def seamlessCloningPoisson(sourceImg, targetImg, mask, offsetX, offsetY):
  
  indexes = getIndexes(mask,targetImg.shape[0],targetImg.shape[1],offsetX,offsetY)
  A = getCoefficientMatrix(indexes)
  b_r = getSolutionVect(indexes,sourceImg[:, :, 0],targetImg[:, :, 0],offsetX,offsetY)
  b_g = getSolutionVect(indexes,sourceImg[:, :, 1],targetImg[:, :, 1],offsetX,offsetY)
  b_b = getSolutionVect(indexes,sourceImg[:, :, 2],targetImg[:, :, 2],offsetX,offsetY)
  x_r = np.linalg.solve(A,b_r) 
  x_g = np.linalg.solve(A,b_g)
  x_b = np.linalg.solve(A,b_b)
  resultImg = reconstructImg(indexes,x_r,x_g,x_b,targetImg)
  return resultImg
  
