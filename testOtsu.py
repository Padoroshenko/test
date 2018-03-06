import matplotlib
import matplotlib.pyplot as plt
from PIL import Image
import cv2
import numpy as np

from pytesseract import image_to_string
import scipy.misc


from skimage.data import page
from skimage.filters import (threshold_otsu, threshold_niblack,
                             threshold_sauvola)


filename = 'frame55'
image = cv2.imread(filename+'.png')
binary_global = image > threshold_otsu(image)

window_size = 25
thresh_niblack = threshold_niblack(image, window_size=window_size, k=0.8)
thresh_sauvola = threshold_sauvola(image)

binary_niblack = image > thresh_niblack
binary_sauvola = image > thresh_sauvola

scipy.misc.imsave(filename+'gl.png', binary_global)
scipy.misc.imsave(filename+'nb.png', binary_niblack)
scipy.misc.imsave(filename+'sa.png', binary_sauvola)


plt.figure(figsize=(8, 7))
plt.subplot(2, 2, 1)
plt.imshow(image, cmap=plt.cm.gray)
plt.title('Original')
plt.axis('off')

plt.subplot(2, 2, 2)
plt.title('Global Threshold')
plt.imshow(binary_global, cmap=plt.cm.gray)
plt.axis('off')

plt.subplot(2, 2, 3)
plt.imshow(binary_niblack, cmap=plt.cm.gray)
plt.title('Niblack Threshold')
plt.axis('off')

plt.subplot(2, 2, 4)
plt.imshow(binary_sauvola, cmap=plt.cm.gray)
plt.title('Sauvola Threshold')
plt.axis('off')

plt.show()
print("OTSU")
print(image_to_string(Image.open(filename+'nb.png'), lang='rus'))
print("NB")
print(image_to_string(Image.open(filename+'nb.png'), lang='rus'))
print("SAV")
print(image_to_string(Image.open(filename+'sa.png'), lang='rus'))