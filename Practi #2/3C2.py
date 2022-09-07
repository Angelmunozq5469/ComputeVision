import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image,ImageFilter

img1 = cv2.imread("TALLER 2 (DEFINIR)/Figura3.png", 0)  # Leemos la imagen
height, width = img1.shape 
imgGb = cv2.GaussianBlur(img1, (3, 3), sigmaX=0, sigmaY=0)  # Aplicamos el kernel a la imagen con la funcion filter2D
#cv2.imshow('Imagen original                               Imagen filtrada', np.hstack([img1,imgGb]))  # Mostramos las imagenes
#cv2.waitKey(0)  # Se espera a pulsar cualquier tecla para cerrar la imagen
#cv2.destroyAllWindows()  # Cierre de ventanas




img3 = cv2.imread("TALLER 2 (DEFINIR)/Figura3.png", 0)  # Leemos la imagen
height, width = img3 .shape[:2]  # Obtenemos sus dimensiones
kern = np.array([[1, -2, 1], [-2, 4, -2], [1, -2, 1]])
imgFpa = cv2.filter2D(img3, ddepth=-1, kernel=kern, anchor=(-1, -1))  # Aplicamos el kernel a la imagen con la funcion filter2D


img4 = cv2.imread("TALLER 2 (DEFINIR)/Figura3.png", 0)  # Leemos la imagen
height, width = img4.shape[:2]  # Obtenemos sus dimensiones
kern1 = np.ones((5, 5),np.float32)/25  # Creamos la matriz del kernel
imgFpb = cv2.filter2D(img4, ddepth=-1, kernel=kern1, anchor=(-1, -1))  # Aplicamos el kernel a la imagen con la funcion filter2D




img5 = cv2.imread("TALLER 2 (DEFINIR)/Figura3.png",0)  # Leemos la imagen
height, width = img5.shape[:2]  # Obtenemos sus dimensiones
kern2 = np.array([[0, -1, 0], [-1, 5, -1], [0, -1, 0]])
imgFsh = cv2.filter2D(img1, ddepth=-1, kernel=kern2, anchor=(-1, -1))  # Aplicamos el kernel a la imagen con la funcion filter2D





img2 = cv2.imread("TALLER 2 (DEFINIR)/Figura3.png", 0)  # Leemos la imagen
height, width = img2.shape[:2]  # Obtenemos sus dimensiones
imgFm = cv2.medianBlur(img2, 3)

cv2.imshow('Imagen original                               Imagen filtrada', np.hstack([img1,imgGb,img2, imgFm,img3,imgFpa,img4,imgFpb,img5,imgFsh]))  # Mostramos las imagenes
cv2.waitKey(0)  # Se espera a pulsar cualquier tecla para cerrar la imagen
cv2.destroyAllWindows()  # Cierre de ventanas