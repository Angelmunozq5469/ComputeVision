from skimage.exposure import rescale_intensity
import numpy as np
import argparse
import cv2
import numpy as np
import matplotlib.pyplot as plt
from PIL import Image,ImageFilter




img_src = cv2.imread("TALLER 1 (2.0)/Tiger.png")
img_src=cv2.resize(img_src,(640, 420))
#prepare the 5x5 shaped filter
kernel = np.array([[1, 1, -1,], 
                    [1, 1, 1], 
                    [1, 1, 1]])
kernel = kernel/sum(kernel)

#filter the source image
img2 = cv2.filter2D(img_src,-1,kernel)

cv2.imshow('Imagen original                               Imagen filtrada', np.hstack([img_src,img2]))  # Mostramos las imagenes
cv2.waitKey(0)  # Se espera a pulsar cualquier tecla para cerrar la imagen
cv2.destroyAllWindows()  # Cierre de ventanas
