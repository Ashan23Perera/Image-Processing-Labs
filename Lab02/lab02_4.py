import cv2
import numpy as np


#=================part 1========================
#masking square
def __masksqr__(I):
    (h,w)    =  I.shape 
    mask_img = np.ones([h,w],dtype=np.uint8)
    for i in range(h - 1):
        for j in range(w - 1):
            if ((i > 63) & (i < 192)):
                if ((j > 63) & (j < 192)):
                    mask_img[i][j] = I[i][j]
    return mask_img     

#===============================================

#================part 2=========================
#masking circle
def __maskcir__(I):
    R = 128 * 128
    (h,w)    =  I.shape 
    mask_img = np.ones([h,w],dtype=np.uint8)
    for i in range(h - 1 ):
        for j in range(w - 1):
            r = pow((i - 128), 2) + pow((j - 128), 2)
            if r < R:
                mask_img[i][j] = I[i][j]
    return mask_img     

#===============================================


#read a image

img    = cv2.imread('images.jpg', 0)
img = cv2.resize(img,(256,256))

#call __masksqr__ function
mask_1_Img = __masksqr__(img)
#call __maskcir__ function
mask_2_Img = __maskcir__(img)

#show the original image
cv2.imshow('Original Image' , img)
#show the Mask Image 1 image
cv2.imshow('Mask  Image  1' , mask_1_Img)
#show the Mask Image 2 image
cv2.imshow('Mask  Image  2' , mask_2_Img)

cv2.waitKey(0)
cv2.destroyAllWindows()
