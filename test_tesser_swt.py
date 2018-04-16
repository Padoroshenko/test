from pytesseract import image_to_string
from PIL import Image


print('File1:')
filename = '1.png'
image = Image.open(filename)
print(image_to_string(image, lang='eng'))

print('File2:')
filename = '2.png'
image = Image.open(filename)
print(image_to_string(image, lang='eng'))