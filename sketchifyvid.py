import cv2
import numpy as np

def sketchvid():
    # define a video capture object
    vid = cv2.VideoCapture(0)

    while True:
        # Capture the video frame by frame
        ret, frame = vid.read()

        # Display the resulting frame
        cv2.imshow('Original video', frame)

        gray=cv2.cvtColor(frame,cv2.COLOR_BGR2GRAY)
        # cv2.imshow('Grayscale', gray)

        inverted_gray_image = 255 - gray
        
        blurred_img = cv2.GaussianBlur(inverted_gray_image, (21,21),0)

        inverted_blurred_img = 255 - blurred_img

        pencil_sketch = cv2.divide(gray, inverted_blurred_img, scale = 256.0)

        cv2.imshow('Sketch effect', pencil_sketch)
        # the 'q' button is set as the quitting button
        if cv2.waitKey(1) & 0xFF == ord('q'):
            break

    # After the loop release the cap object
    vid.release()
    # Destroy all the windows
    cv2.destroyAllWindows()
