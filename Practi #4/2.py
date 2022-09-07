#Types of tracking
#1. Video tracking (Real time, Recorded videos)Q
#2. Visual tracking (Everyday scenarios, estimate position)
#3. Image tracking (Dataset)
#4. Object tracking camera (Tracking helmet, Tracking vest)
#Conclusion el mejor metodo que podemos utilizar es
#Video tracking


import numpy as np
import cv2 as cv
cap=cv.VideoCapture("TALLER 4 (DEFINIR)/videoclase2.mp4")


obj_detector=cv.createBackgroundSubtractorMOG2() #history=100,varThreshold=0



while True:
    ret,frame=cap.read()
    
    height, width, _=frame.shape
    
    margen=frame[100: 554, 120:450]
    
    mascara=obj_detector.apply(margen)
    
#   _, mascara=cv.threshold(mascara,254,255,cv.THRESH_BINARY)
    
    contornos, _ =cv.findContours(mascara,cv.RETR_TREE,cv.CHAIN_APPROX_SIMPLE)
    

    for cnt in contornos:
        area=cv.contourArea(cnt)
        if area>100:
            
            #cv.drawContours (margen,[cnt],-1,(0,255,0),2)
            
            x,y,w,h=cv.boundingRect(cnt)
            
            cv.rectangle(margen,(x,y),(x+w,y+h),(0,255,0),3)
            
            print(x,y,w,h)
            
    cv.imshow("margen",margen)
    cv.imshow('frame',frame)
    cv.imshow('mask',mascara)
    
    key=cv.waitKey(50)
    if key == ord("q"):
        break

cv.destroyAllWindows()

