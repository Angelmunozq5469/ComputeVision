import cv2 as cv
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image,ImageFilter

img=Image.open("TALLER 2 (DEFINIR)/2.png")

img=img.filter(ImageFilter.GaussianBlur(radius=35))

img.show()



import numpy as np
import cv2

img1 = cv2.imread("TALLER 2 (DEFINIR)/2.png", 0)  # Leemos la imagen
height, width = img1.shape  # Obtenemos sus dimensiones
imgGb = cv2.GaussianBlur(img1, (35, 35), sigmaX=0, sigmaY=0)  # Aplicamos el kernel a la imagen con la funcion filter2D
cv2.imshow(f"Imagen original   Imagen filtrada", np.hstack([img1,imgGb]))  # Mostramos las imagenes
cv2.imwrite("TALLER 2 (DEFINIR)/imagemodificadaA.png",imgGb)
cv2.waitKey(0)  # Se espera a pulsar cualquier tecla para cerrar la imagen
cv2.destroyAllWindows()  # Cierre de ventanas
# Fuente: Documentacion OpenCV