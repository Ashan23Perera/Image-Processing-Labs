import cv2
import numpy as np
import matplotlib
import matplotlib.pyplot as plt


#==================part 1=======================
#Use inbuilt  OpenCV cv2.calcHist() function
def __hist__(I,figno):
    hist = cv2.calcHist([I],[0],None,[256],[0,256])
    N = len(hist)
    x = range(N)
    width = 0.75
    plt.figure(figno)
    plt.bar(x, hist, width, color = 'blue')
    plt.title('OpenCV cv2.calcHist() function')

#===============================================


#=================part 2========================
#Use inbuilt  numpy np.histogram() function     
def __histo__(I, figno):
    hist,bins = np.histogram(I.ravel(),256,[0,256])
    N = len(hist)
    x = range(N)
    width = 0.75
    plt.figure(figno)
    plt.bar(x, hist, width, color = 'blue')
    plt.title('Numpy np.histogram() function')
#===============================================


#===============================================
def __histogramGrey__(I):
    (h, w) = I.shape
    array = np.zeros(256)
    for i in range(h):
        for j in range(w):
            array[I[i][j]] = array[I[i][j]] + 1 
    return array    
#=========================================

#=========================================
def __histogramRGB__(I):
    h = 174
    w = 290
    R_img = np.ones([h,w],dtype = np.uint8)
    G_img = np.ones([h,w],dtype = np.uint8)
    B_img = np.ones([h,w],dtype = np.uint8)
    for i in range(h - 1):
        for j in range(w - 1):
            R_img[i][j] = I[i][j][0]
            G_img[i][j] = I[i][j][1]
            B_img[i][j] = I[i][j][2]

    array = [R_img, B_img, G_img]
    return array
#=========================================

#=========================================
def __histogram__(I, col, figno):
    array = __histogramGrey__(I) 
    N = len(array)
    x = range(N)
    width = 0.75
    plt.figure(figno)
    plt.bar(x, array, width, color = col)
    plt.title(' Histogram plot for a grayscale image')
#=========================================

#=========================================
def __histogramMultiple__(I, col, figno):
    array = __histogramRGB__(I)
    array = [__histogramGrey__(array[0]),__histogramGrey__(array[1]),__histogramGrey__(array[2]) ]
    N = len(array[0])
    x = range(N)
    width = 0.75
    plt.figure(figno)
    for i in range(1 , 4):
        plt.subplot(3,1,i), plt.bar(x, array[i - 1], width, color = col[i - 1])
        if i == 1:
            plt.title('Histogram plot for a RGB image')    

#=========================================


#read a image
imgGrey   = cv2.imread('images.jpg', 0)        
imgRGB    = cv2.imread('images.jpg', 1)
colour = ['red','green','blue']

#display histogram

#cv2.calcHist() functon
__hist__(imgGrey, 1)
#np.histogram() function
__histo__(imgGrey, 2)
# Show a histogram plot for a grayscale image
__histogram__(imgGrey, 'blue', 3)
# Show three histograms for a given RGB image
__histogramMultiple__(imgRGB, colour, 4)

plt.show()

cv2.waitKey(0)
cv2.destroyAllWindows()
