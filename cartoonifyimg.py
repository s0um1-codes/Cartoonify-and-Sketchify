import cv2
import numpy as np

def cartoonimg():
        import easygui
        ImagePath=easygui.fileopenbox()

        img = cv2.imread(ImagePath)
        rs1 = cv2.resize(img, (550, 450))
        # Display the resulting frame
        cv2.imshow('Original Photo', rs1)
        
        #convert to gray scale
        grayImage = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)
        
        #apply gaussian blur
        grayImage = cv2.GaussianBlur(grayImage, (3, 3), 0)
        
        #detect edges
        edgeImage = cv2.Laplacian(grayImage, -1, ksize=5)
        edgeImage = 255 - edgeImage
        
        #threshold image
        ret, edgeImage = cv2.threshold(edgeImage, 150, 255, cv2.THRESH_BINARY)

        #blur images heavily using edgePreservingFilter
        edgePreservingImage = cv2.edgePreservingFilter(img, flags=2, sigma_s=50, sigma_r=0.4)
        
        #create output matrix
        output = np.zeros(grayImage.shape)
        
        #combine cartoon image and edges image
        cartoon = cv2.bitwise_and(edgePreservingImage, edgePreservingImage, mask=edgeImage)

        rs2 = cv2.resize(cartoon, (550, 450))
        cv2.imshow('Cartoon effect', rs2)
