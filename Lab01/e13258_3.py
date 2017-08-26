import cv2
import numpy as np


#Function of Flipped image on Y axis
#=========================================

def __flipud__(I):
    (h,w) =  I.shape 
    flipy_img = np.ones([h,w],dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            flipy_img[i][j]  =  I[i][w - j - 1]

    return flipy_img

#=========================================

#Test the __imcomplement__() function 

#read a image
img    = cv2.imread('download.jpg',0)

#show the original image
cv2.imshow('Original' , img)

#call the __flipud__() function
Image = __flipud__(img)

#show the Flipped image in Y axis
cv2.imshow('Flipped image in Y axis' , Image)


cv2.waitKey(0)
cv2.destroyAllWindows()
