import cv2
import math
import numpy as np
from matplotlib import pyplot as plt

#==============part 1===========================
#use c * log(1 + r)  
def __logTransform__(I, c):
    (h,w) =  I.shape 
    log_img = np.ones([h,w],dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            l             = c * math.log(int(I[i][j]) + 1)
            log_img[i][j] = l                
    return log_img     

#===============================================

#===============part 2==========================
#use c * (r ^ gamma)
def __powerTransform__(I, c, gamma):
    (h,w) =  I.shape 
    pow_img = np.ones([h,w],dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            l = int(c * math.pow(int(I[i][j]), gamma))
            if l > 255:
                l = 255
            pow_img[i][j] = l 
    return pow_img     

#===============================================

#================part 3=========================
def __greyLevel__(I, minimum, maximum):
    (h,w) =  I.shape 
    grey_img = np.ones([h,w],dtype=np.uint8)
    for i in range(h):
        for j in range(w):
            if ((I[i][j] < maximum) & (I[i][j] > minimum)):
                grey_img[i][j] = I[i][j]
    return grey_img     

#===============================================

#================part 4=========================

def __binary__(number, k):
    return ((number >> k) & 1)

def __bitLevel__(I, k):
    (h,w) =  I.shape
    bit_img = np.ones([h,w],dtype=np.uint8) 
    for i in range(h):
        for j in range(w):
            l = 0
            if (__binary__(int(I[i][j]), k) == 1):
                l = 255
            bit_img[i][j] = l   
    return  bit_img
    
#===============================================



#read a image
img    = cv2.imread('images.jpg', 0)

#log transformation c = 10
logImg  = __logTransform__(img, 10)
#power transformation c = 20 gamma = 0.50
powImg  = __powerTransform__(img, 20, 0.50)
#grey level slicing
greyImg = __greyLevel__(img, 70, 170)
#bit plane slicing
bit = []
for i in range(8):
    bit.append( __bitLevel__(img, i))



#show the original image
cv2.imshow('Original Image' , img)

#show the log transformation image
cv2.imshow('Log Transfom Image' , logImg)

#show the log transformation image
cv2.imshow('Pow Transfom Image' , powImg)

#show the grey level slicing image
cv2.imshow('Grey Level Transform' , greyImg)

#show the bit plane slicing

for i in range(1,9):
    plt.subplot(3,3,i), plt.imshow(bit[i - 1], 'gray')
plt.subplot(3,3,9), plt.imshow(img, 'gray')

plt.show()


cv2.waitKey(0)
cv2.destroyAllWindows()
