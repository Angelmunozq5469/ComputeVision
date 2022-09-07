from tokenize import Imagnumber
import cv2
import numpy as np

cap = cv2.VideoCapture(0)

while True:
    # Captura cuadro a cuadro
    _, frame = cap.read()
    
    # Conversion de la captura a escala de grises
    
    gray = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY)
    _, thresh1 = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)  # Umbralizacion con operador binario
    cv2.imwrite('Barras.png', thresh1)
    cv2.imshow('video1', frame)
    cv2.imshow('video2', thresh1)
    if cv2.waitKey(1) & 0xFF == ord('q'): # Se esperan 30ms para el cierre de la ventana o hasta que el usuario precione la tecla q
        break

cap.release()

cv2.destroyAllWindows()


img1 = cv2.imread('Barras.png')
gray = cv2.cvtColor(img1, cv2.COLOR_BGR2GRAY)
_, thresh1 = cv2.threshold(gray, 100, 255, cv2.THRESH_BINARY)
height, width = thresh1.shape[:2]  # Obtenemos sus dimensiones

lineas = []
c = 0
for i in range (len(thresh1)):
    if i == round(len(thresh1)/2):
        for j in range (len(thresh1[0])):
            if thresh1[i][j] == 255:
                c = c+1
            else:
                if c != 0:
                    lineas.append(c)
                c = 0

barra = int(input('Ingresa el numero de barra que quieres conocer su ancho en pixeles: '))
print(lineas[(barra-1)])




