import cv2
import numpy as np


#=========================================
def __addition__(I1, I2):
    (h1,w1) =  I1.shape
    (h2,w2) =  I2.shape
    add_img = np.ones([h1,w1],dtype=np.uint8)
    for i in range(h1-1):
        for j in range(w1-1):
            l =  int(I1[i][j]) + int(I2[i][j])
            if l > 255:
                l = 255
            add_img[i][j] = l
            
    return add_img     

#=========================================


#=========================================
def __substraction__(I1, I2):
    (h1,w1) =  I1.shape
    (h2,w2) =  I2.shape
    sub_img = np.ones([h1,w1],dtype=np.uint8)
    for i in range(h1):
        for j in range(w1):
            l  = int(I1[i][j]) - int(I2[i][j])
            if l < 0:
                l = 0
            sub_img[i][j] = l 
    return sub_img     

#=========================================



image1   =  raw_input("Enter the image 1(rabbit.jpg): ")
image2   =  raw_input("Enter the image 2(monkey.jpg): ");

#read a image
img1    = cv2.imread(image1, 0)
img2    = cv2.imread(image2, 0)

added_img = __addition__(img1, img2)
subtr_img = __substraction__(img1, img2)

#show the original image
cv2.imshow('Original Image 1' , img1)
cv2.imshow('Original Image 2' , img2)

#show the added image
cv2.imshow('Image Addition' , added_img)
#show the substract image
cv2.imshow('Image Substraction' , subtr_img)


cv2.waitKey(0)
cv2.destroyAllWindows()
