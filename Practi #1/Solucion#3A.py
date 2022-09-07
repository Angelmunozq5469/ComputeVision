import cv2 as cv
import numpy as np



img=cv.imread("Tiger.png",0)
rows,cols=img.shape;Un=cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),10,1)
img_mod=cv.warpAffine(img,Un,(cols,rows))

width=700; height=450;medidas=(width,height);imag4=cv.resize(img_mod,medidas,interpolation=cv.INTER_AREA)



cv.imshow("img",imag4)
cv.waitKey(0)




img=cv.imread("Tiger.png",0)
Ti=np.float32([[1,0.5,0],[0.5,1,0],[0,0,1]])
rows,cols=img.shape;Yt=cv.warpPerspective(imag4,Ti,(int(cols*1.5),int(rows*1.5)))

cv.imshow("img3",Yt)
cv.waitKey(0)



Te=np.float32([[1,0,50],[0,1,50]])
Ru=cv.warpAffine(Yt,Te,(cols,rows))
cv.imshow("img2",Ru)
cv.waitKey(0)