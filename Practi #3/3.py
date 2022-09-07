from telnetlib import theNULL
from xml.dom.expatbuilder import theDOMImplementation
import cv2 as cv
import numpy as np

img=cv.imread("pyimageok/img1.png")

img1=cv.cvtColor(img, cv.COLOR_BGR2GRAY)
ret,thresh1=cv.threshold(img1,120,255,cv.THRESH_BINARY,cv.THRESH_OTSU)



contorno, iluminacion=(cv.findContours(thresh1,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE))
img_contorno=np.zeros(img.shape)
cv.drawContours(img_contorno,contorno,-1,(0,255,0),3)




#cv.imshow('otsu.png',thresh1)
#cv.waitKey(0)
#cv.destroyAllWindows()

#cv.imwrite('contorno.png',img_contorno)
#cv.waitKey(0)
#cv.destroyAllWindows()



