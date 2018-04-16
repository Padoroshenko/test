import pillowfight
from PIL import Image,ImageOps

i=0
#while True:
    #i = i + 1
    #filename = 'frames/frame' + str(i) + '.png'
filename = "cv.jpg"
img_in = Image.open(filename)
#if not (img_in):
#    break
width = img_in.size[0]
height = img_in.size[1]
img_in_neg = ImageOps.invert(img_in)
img_out1 = pillowfight.swt(img_in, output_type=pillowfight.SWT_OUTPUT_ORIGINAL_BOXES)
img_out1.save("1.png")
img_out2 = pillowfight.swt(img_in_neg, output_type=pillowfight.SWT_OUTPUT_ORIGINAL_BOXES)
#img_out2.save('frames/frame' + str(i) + '(n)' + '.png')
img_out2.save('2.png')