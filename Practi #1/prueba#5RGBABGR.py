import cv2 as cv

img=cv.imread("Tiger.png")

img_rgb=cv.cvtColor(img,cv.COLOR_RGB2BGR)
 
cv.imshow("img23",img_rgb)
cv.waitKey(0)
