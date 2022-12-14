# -*- coding: utf-8 -*-
"""PCD_Image-Enhancement.ipynb

Automatically generated by Colaboratory.

Original file is located at
    https://colab.research.google.com/drive/1wE20nxOpFHqjZmqbVJj2C9sVQaUpjm9x
"""

import cv2
import numpy as np
from google.colab.patches import cv2_imshow
from google.colab import drive
drive.mount('/content/drive')
from matplotlib import pyplot as plt

"""variabel untuk membaca gambar"""

image = cv2.imread("/content/drive/MyDrive/imagesaya.jpg")

"""menampilkan gambar"""

print("image")
cv2_imshow(image)

"""Menampilkan dimensi gambar"""

print("image")
print(image.shape)

"""Mengkonversi warna"""

imageabu = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
imagergb = cv2.cvtColor(image, cv2.COLOR_BGR2RGB)
imagehsv = cv2.cvtColor(image, cv2.COLOR_BGR2HSV)

"""Menampilkan hasil konversi warna"""

print("IMAGE ABU")
cv2_imshow(imageabu)
print("IMAGE RGB")
cv2_imshow(imagergb)
print("IMAGE HSV")
cv2_imshow(imagehsv)

"""Memisahkan channel BGR"""

B,G,R = cv2.split(image)

print("Blue")
cv2_imshow(B)
print("Grey")
cv2_imshow(G)
print("Red")
cv2_imshow(R)

gabung = cv2.merge([B,G,R])
print("Gabung BGR")
cv2_imshow(gabung)

gabungRGB = cv2.merge([R,G,B])
print("Gabung RGB")
cv2_imshow(gabungRGB)

"""HSV"""

H,S,V = cv2.split(image)
print("Hue")
cv2_imshow(H)
print("Saturation")
cv2_imshow(S)
print("Value")
cv2_imshow(V)

gabungHSV = cv2.merge([H,S,V])
print("Gabung")
cv2_imshow(gabungHSV)

"""Menggunakan MathPlotLib"""

plt.figure(figsize=[15,15])
plt.subplot(221)
plt.imshow(B)
plt.subplot(222)
plt.imshow(G)
plt.subplot(223)
plt.imshow(R)
plt.subplot(224)
plt.imshow(gabungRGB)
plt.show()