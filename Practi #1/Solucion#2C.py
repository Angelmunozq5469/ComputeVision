import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from pyparsing import col

img=cv.imread("2B.png"); img=cv.cvtColor(img,cv.COLOR_BGR2RGB)

plt.axis("off")


rows,cols,dim=img.shape

angulo=np.radians(10)

T=np.float32([[np.cos(angulo), -(np.sin(angulo)),0],
            [np.sin(angulo),np.cos(angulo),0],
            [0,0,1]])

rotacion_img=cv.warpPerspective(img,T,(int(cols),int(rows)))

plt.axis("off")

plt.imshow(rotacion_img)
plt.show()

plt.imsave("2C.png",rotacion_img)