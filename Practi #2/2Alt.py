from skimage.exposure import rescale_intensity
import numpy as np
import argparse
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image,ImageFilter




img1= cv2.imread("TALLER 1 (2.0)/Tiger.png", 0)
img2 = cv2.resize(img1, (640, 420))
height, width = img2 .shape[:2]
#kern = np.array([[0, -1, 0], [-1, 4, -1], [0, -1, 0]])
kern = np.array([[-1, -1, -1], [-1, 8, -1], [-1, -1, -1]])
imgFpa = cv2.filter2D(img2, ddepth=-1, kernel=kern, anchor=(-1, -1))  # Aplicamos el kernel a la imagen con la funcion filter2D
cv2.imshow('Imagen original                               Imagen filtrada', np.hstack([img2, imgFpa]))  # Mostramos las imagenes
cv2.waitKey(0)  # Se espera a pulsar cualquier tecla para cerrar la imagen
cv2.destroyAllWindows()  # Cierre de ventanas



