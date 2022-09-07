import cv2 as cv


#Comparacion Histogramas

#La comparacion de histogramas se fundamenta en la cantidad de pixeles que hay presentes en una imagen por ende
#si comparamos imagenes similares tomadas en dos ocasiones diferentes podremos cuantificar que tanta similitud 
#teorica hay entre ambas. 

#Funcionamiento

#Los histogramas de imagen consisten en un resumen visual que muestra la 
# distribución de una variable numérica continua midiendo la frecuencia con la que determinados valores que aparecen en la imagen. 
# En el histograma de imagen, el eje x es una línea numérica que visualiza el rango de valores de píxeles de
# la imagen que se ha dividido en rangos de números o bins. Se dibuja para cada bin una barra en la que el
# ancho de la barra representa el rango de números de densidad del bin y la altura de la barra representa 
# el número de píxeles incluidos en ese rango. permite conocer la distribución de los datos 
#siendo importante para la exploracion de los datos.


#Apliacion

#Su aplicacion es diversa pero agrandes razgos con los histograma se puede evaluar la calidad de una imagen
#entonces si obtenemos un histograma con perdida de pixeles o aderidos a extremos de los Ejes tanto X como Y tendra
# una repercucion notable a la hora de analizar la imagen.  


#Como se usa en OPENCV Y APLICACION PRACTICA
#OPENCV contiene una funcion que sirve para comparar los histogramas de las imagenes, la funcion se llama
#CompareHist().

import cv2 as cv
import numpy as np

base = cv.imread('1C.png');width=700; height=450;medidas=(width,height);base=cv.resize(base,medidas,interpolation=cv.INTER_AREA)
test = cv.imread('2C.png');width=700; height=450;medidas=(width,height);test=cv.resize(test,medidas,interpolation=cv.INTER_AREA)




hsv_base = cv.cvtColor(base, cv.COLOR_BGR2HSV)
hsv_test = cv.cvtColor(test, cv.COLOR_BGR2HSV)

h_bins = 50
s_bins = 60
histSize = [h_bins, s_bins]
h_ranges = [0, 180]
s_ranges = [0, 256]
ranges = h_ranges + s_ranges
channels = [0,1]

hist_base = cv.calcHist([hsv_base], channels, None, histSize, ranges, accumulate=False)
cv.normalize(hist_base, hist_base, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)
hist_test = cv.calcHist([hsv_test], channels, None, histSize, ranges, accumulate=False)
cv.normalize(hist_test, hist_test, alpha=0, beta=1, norm_type=cv.NORM_MINMAX)


compare_method = cv.HISTCMP_CORREL


base_test = cv.compareHist(hist_base, hist_test, compare_method)


print('base_test Similarity = ', base_test)


cv.imshow('base',base)
cv.imshow('test1',test)

cv.waitKey(0)
