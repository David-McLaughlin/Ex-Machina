#####################################################
# Simple little program to extract text from images 
# Review README for set up
# Executed on WSL ( Ubuntu 20.04 ) 
#####################################################
from PIL import Image
import pytesseract
import numpy as np

filename = '/filepath/poem.png'
img1 = np.array(Image.open(filename))
text = pytesseract.image_to_string(img1)
print(text)
