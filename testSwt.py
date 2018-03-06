import pillowfight
from PIL import Image,ImageOps


filename = "input1.jpg"

img_in = Image.open(filename)
width = img_in.size[0]
height = img_in.size[1]
img_in_neg = ImageOps.invert(img_in)
img_out1 = pillowfight.swt(img_in, output_type=pillowfight.SWT_OUTPUT_ORIGINAL_BOXES)
img_out1.save("output1.jpg")
img_out2 = pillowfight.swt(img_in_neg, output_type=pillowfight.SWT_OUTPUT_ORIGINAL_BOXES)
img_out2.save("output2.jpg")