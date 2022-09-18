import cv2
import numpy as np

def sketchimg():
        import easygui
        ImagePath=easygui.fileopenbox()

        img = cv2.imread(ImagePath)
        rs1 = cv2.resize(img, (550, 450))
        # Display the resulting frame
        cv2.imshow('Original Photo', rs1)
        
        gray=cv2.cvtColor(img,cv2.COLOR_BGR2GRAY)
        # cv2.imshow('Grayscale image', gray)

        inverted_gray_image = 255 - gray
        # cv2.imshow('Inverted Grayscale image', gray)

        blurred_img = cv2.GaussianBlur(inverted_gray_image, (21,21),0)
        # cv2.imshow('Blurred image', blurred_img)

        inverted_blurred_img = 255 - blurred_img
        # cv2.imshow('Inverted Blurred image', inverted_blurred_img)

        pencil_sketch_img = cv2.divide(gray, inverted_blurred_img, scale = 256)

        rs2 = cv2.resize(pencil_sketch_img, (550, 450))
        cv2.imshow('Sketch effect', rs2)
