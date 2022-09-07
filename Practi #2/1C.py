import cv2 
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image,ImageFilter



imgA=cv2.imread("TALLER 2 (DEFINIR)/2.png",0)
imgB=cv2.imread("TALLER 2 (DEFINIR)/B.png",0)
height,width=imgA.shape
height1,width1=imgB.shape
imgC1=cv2.addWeighted(imgA,0.3,imgB,0.7,-34)
cv2.imshow("IMAGEN A                                                                 IMAGEN B                                                                              IMAGEN C",np.hstack([imgA, imgB,imgC1]))
cv2.waitKey(0)
cv2.destroyWindow()