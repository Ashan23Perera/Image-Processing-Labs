import cv2
import numpy as np


#=========================================
def __threshold__(I, threshValue):
    (h,w) =  I.shape 
    inv_img = np.ones([h,w],dtype=np.uint8)
    for i in range(h - 1 ):
        for j in range(w - 1):
            if (I[i][j] < threshValue):
                inv_img [i][j] = 255;
            else:
                inv_img [i][j] = 0;
                
    return inv_img     

#=========================================


#read a image

val   = input("Enter threshold value: ")
image = raw_input("Enter the image(moon.jpeg): ");
img    = cv2.imread(image, 0)

#call the __threshold__ function
threshImg = __threshold__(img, val)

#show the original image
cv2.imshow('Original Image' , img)

#show the threshold image
cv2.imshow('Threshold Image' , threshImg)


cv2.waitKey(0)
cv2.destroyAllWindows()
