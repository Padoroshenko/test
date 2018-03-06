from pytesseract import image_to_string
from PIL import Image


print('File1:')
filename = 'output1.jpg'
image = Image.open(filename)
print(image_to_string(image, lang='eng'))

print('File2:')
filename = 'output2.jpg'
image = Image.open(filename)
print(image_to_string(image, lang='eng'))