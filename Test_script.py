import matplotlib.pyplot as plt
from seamlessCloningPoisson import seamlessCloningPoisson

sourceImg = plt.imread("SourceImage.png")
targetImg = plt.imread("TargetImage.png")
mask = plt.imread("minionMask.png")
offsetX = 100
offsetY = 100
result = seamlessCloningPoisson(sourceImg,targetImg,mask,offsetX,offsetY)
plt.imsave("result.png",result)
  
