import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img=cv.imread("TALLER 1 (2.0)/Tiger.png")

img=cv.cvtColor(img,cv.COLOR_BGR2RGB)

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

#plt.imsave("1A.png",rotacion_img)



