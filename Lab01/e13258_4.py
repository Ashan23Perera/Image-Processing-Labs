import cv2
import math
import numpy as np


#Function of resize a image using with nearest­neighbour interpolation 

#=========================================
def __imresize__(I, x, y):
    resize_img = np.ones([x,y],dtype=np.uint8)
    (h,w) =  I.shape
    (h1,w1) = resize_img.shape
    for i in range(h1):
        l = int((i * h)/h1)
        for j in range(w1):
            r = int((j * w)/w1)
            resize_img[i][j] = img[l][r]

    return resize_img

#=========================================

#Test the __imresize__() function 

#read a image
img    = cv2.imread('download.jpg',0)

#Enter your desired values x and y
x = input('Enter x value: ')
y = input('Enter y value: ')

#show the original image
cv2.imshow('Original' , img)

#call the __inresize__() function
Image = __imresize__(img, x, y)

#show the resize image
cv2.imshow('Resize Image' , Image)


cv2.waitKey(0)
cv2.destroyAllWindows()

