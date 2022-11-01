import pytesseract
import cv2
import sys
####################################################################
# Take the image as a parameter from command line arg using OpenCV #
####################################################################
image = cv2.imread(sys.argv[1])

###################################
# Extract the text from the image #
###################################
string = pytesseract.image_to_string(image)

############################
# Print the extracted Text #
############################
print(string)

##############
# Print Data #
##############
#data = pytesseract.image_to_data(image)
#print(data)
