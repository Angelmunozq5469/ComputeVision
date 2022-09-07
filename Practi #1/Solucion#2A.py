import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from pyparsing import col

img=cv.imread("Tiger.png"); img=cv.cvtColor(img,cv.COLOR_BGR2RGB)

plt.axis("off")


rows,cols,dim=img.shape



To=np.float32([[1,0,50],[0,1,50],[0,0,1]])

trasladar_img=cv.warpPerspective(img,To,(cols,rows))

plt.axis("off")

plt.imshow(trasladar_img)
plt.show()

plt.imsave("2A.png",trasladar_img)
