'''
  File name: getIndexes.py
  Author: Vaishak Kumar, Cathleen Gui
  Date created:
'''

'''
Function indexes replacement pixels in the target image to as to reduce calculations.
(INPUT) mask: The logical matrix h×w representing the replacement region.
(INPUT) targetH: The height of the target image, h'
(INPUT) targetW: The width of the target image, w'
(INPUT) offsetX: The x-axis offset of the source image with respect to the target image.
(INPUT) offsetY: The y-axis offset of the source image with respect to the target image.
(OUTPUT) indexes: h'×w' matrix representing the indices of each replacement pixel. The value 0 means that is not a replacement pixel.
'''

'''
'''
import numpy as np
import matplotlib.pyplot as plt

def getIndexes(mask, targetH, targetW, offsetX, offsetY):
  #Pixel Counter
  Index = 1
  indexes = np.zeros((targetH,targetW), dtype = "int32")
  for i in range(mask.shape[0]):
    for j in range(mask.shape[1]):
      if mask[i,j] != 0:
        indexes[offsetY+i,offsetX+j] = Index
        Index = Index + 1
  return indexes