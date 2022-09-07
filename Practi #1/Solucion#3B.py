import cv2 as cv
import numpy as np

img=cv.imread("Tiger.png",0);width=700; height=450;medidas=(width,height);img=cv.resize(img,medidas,interpolation=cv.INTER_AREA)

Matriz=np.float32([[1,0,50],[0,1,50]])

rows,cols=img.shape;transformacion_1=cv.warpAffine(img,Matriz,(cols,rows))
cv.imshow("prueba",transformacion_1)
cv.waitKey(0)


Matriz2=np.float32([[1,0.5,0],[0.5,1,0],[0,0,1]])
rows,cols=img.shape;transformacion_2=cv.warpPerspective(transformacion_1,Matriz2,(int(cols*1.5),int(rows*1.5)))

cv.imshow("prueba2",transformacion_2)
cv.waitKey(0)


Matriz3=cv.getRotationMatrix2D(((cols-1)/2.0,(rows-1)/2.0),10,1)
transformacion_3=cv.warpAffine(transformacion_2,Matriz3,(cols,rows))
cv.imshow('prueba3',transformacion_3)
cv.waitKey(0)