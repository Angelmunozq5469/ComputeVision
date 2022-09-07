import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt


img=cv.imread("1A.png"); img=cv.cvtColor(img,cv.COLOR_BGR2RGB)

plt.axis("off")


rows,cols,dim=img.shape


T=np.float32([[1,0.5,0],
               [0.5,1,0],
               [0,0,1]])

she_img=cv.warpPerspective(img,T,(int(cols*1.5),int(rows*1.5)))

plt.axis("off")

plt.imshow(she_img)
plt.show()

#plt.imsave("1B.png",she_img)

