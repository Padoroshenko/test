from PIL import Image
from pathlib import Path
from skimage.filters import (threshold_sauvola)
import scipy.misc
import cv2


i=22

while True:
 i=i+1
 filename = 'frames/frame' + str(i) +'.png'
 imgfile = Path(filename)
 if not imgfile:
  break
 img = Image.open(imgfile)
 img3 = img.crop( (0,322,640,343) ).save(filename)
 image = cv2.imread(filename)
 thresh_sauvola = threshold_sauvola(image)
 binary_sauvola = image > thresh_sauvola
 scipy.misc.imsave(filename, binary_sauvola)

