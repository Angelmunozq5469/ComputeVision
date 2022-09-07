from colorsys import rgb_to_hls
import os
import matplotlib.image as image
import numpy as np
import cv2
import matplotlib.pyplot as plt
img=image.imread("TALLER 1 (2.0)/Tiger.png")
print("The shape of the image is:",img.shape)
print("the image as array is:")
print(img)

a=np.array([[img]])
print(np.median(a))
