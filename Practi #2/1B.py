import cv2 
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image,ImageFilter

img1 = cv2.imread("TALLER 2 (DEFINIR)/B.png", 0)  # Leemos la imagen
height, width = img1.shape  # Obtenemos sus dimensiones
imgGb = cv2.GaussianBlur(img1, (35, 35), sigmaX=0, sigmaY=0)  # Aplicamos el kernel a la imagen con la funcion filter2D
cv2.imshow(f"Imagen original",img1)  # Mostramos las imagenes
cv2.waitKey(0)  # Se espera a pulsar cualquier tecla para cerrar la imagen
cv2.destroyAllWindows()  # Cierre de ventanas
# Fuente: Documentacion OpenCV


