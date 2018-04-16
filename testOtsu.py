from PIL import Image
from pathlib import Path
from skimage.filters import (threshold_sauvola)
import scipy.misc
import cv2

filename = "res.jpg"
imgfile = Path(filename)

img = Image.open(imgfile)
image = cv2.imread(filename)
thresh_sauvola = threshold_sauvola(image)
binary_sauvola = image > thresh_sauvola
scipy.misc.imsave(filename, binary_sauvola)

