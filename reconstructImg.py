'''
  File name: reconstructImg.py
  Author: Vaishak Kumar, Cathleen Gui
  Date created:
'''
'''
Function solves for vector x given coefficient matrix A and solution vector b.
Replaces pixels in target image with updated intensity.
(INPUT) indexes: h'×w' matrix representing the indices of each replacement pixel.
(INPUT) red: 1×N vector representing the intensity of the red channel replacement pixel.
(INPUT) green: 1×N vector representing the intensity of the green channel replacement pixel. 
(INPUT) blue: 1×N vector representing the intensity of the blue channel replacement pixel. 
(INPUT) targetImg: h'×w'×3 matrix representing the target image. 
(OUTPUT) resultImg: h'×w'×3 matrix representing the resulting cloned image. 
'''

def reconstructImg(indexes, red, green, blue, targetImg):
  resultImg = targetImg.copy()
  for i in range(indexes.shape[0]):
    for j in range(indexes.shape[1]):
      if indexes[i,j] != 0:
        resultImg[i,j,0] = red[indexes[i,j]-1]
        resultImg[i,j,1] = green[indexes[i,j]-1]
        resultImg[i,j,2] = blue[indexes[i,j]-1]
  return resultImg