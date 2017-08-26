import cv2
import numpy as np


#Function of Inverting a image
#=========================================
def __imcomplement__(I):
    (h,w) =  I.shape 
    inv_img = np.ones([h,w],dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            inv_img [i][j] = 255 - I[i][j] 

    return inv_img     

#=========================================
imge = np.ones([255,255],dtype=np.uint8)
for i in range(255):
    for j in range(255):
        imge [i][j] = 255 

cv2.imshow('Original' , imge)

''' 
#Test the __imcomplement__() function 

#read a image
img    = cv2.imread('download.jpg',0)
print img
#show the original image
cv2.imshow('Original' , img)

#call the __imcomplement__ function
Image = __imcomplement__(img)

#show the inverted image
cv2.imshow('Inverted' , Image)
'''

cv2.waitKey(0)
cv2.destroyAllWindows()
