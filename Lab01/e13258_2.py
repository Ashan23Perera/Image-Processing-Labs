import cv2
import numpy as np



#Function of Flipped image on X axis
#=========================================

def __fliplr__(I):
    (h,w) =  I.shape 
    flipx_img = np.ones([h,w],dtype=np.uint8)
    for i in range(w):
        for j in range(h):
            flipx_img[j][i] =  I[h - j - 1][i] 
    return flipx_img 
     

#=========================================

#Test the __imcomplement__() function 

#read a image
img    = cv2.imread('download.jpg',0)

#show the original image
cv2.imshow('Original' , img)

#call the __fliplr__() function
Image = __fliplr__(img)

#show the Flipped image in X axis
cv2.imshow('Flipped image in X axis' , Image)


cv2.waitKey(0)
cv2.destroyAllWindows()
        


