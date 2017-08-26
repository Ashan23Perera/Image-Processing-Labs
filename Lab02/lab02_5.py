import cv2
import numpy as np


#=========================================
#use image arithmatic  operators (image + scaler value)
def addbrightness(I, value):
    (h,w) =  I.shape 
    bri_img = np.ones([h,w],dtype=np.uint8)
    for i in range(h - 1 ):
        for j in range(w - 1):
            l = int(I[i][j]) + value
            if (l > 255):
                l = 255
            bri_img[i][j] = l 
            
    return bri_img     

#=========================================


#read a image
val = input("Enter required value for brighter the image: ")

#read the image
img    = cv2.imread('images.jpg', 0)

#call addbrightness function
briteImg = addbrightness(img, val)

#show the original image
cv2.imshow('Original Image' , img)
#show the briteness image
cv2.imshow('Threshold Image' , briteImg)


cv2.waitKey(0)
cv2.destroyAllWindows()

