#RUN THIS
#Open Cv capture the image/stream.
#Convert rgb to hsv, color_ extract one colour that we need (hue saturation value)
#remove noise from image (extra data that we do not need) Gaussian blur to the hsv converted image.

# Searching contours
# Navigate the car.
''' first erodes the image and then dilates it morph close
dilates the image and then erodes it
transforma to the Gaussian blurred image.'''
import cv2                            #
import imutils                        #functions to make basic image processing
from imutils.video import VideoStream #
import numpy as np                    #
from directkeys import A, D, W, ReleaseKey, PressKey #

cam = VideoStream(src=0).start()      # camera
currentKey=list()                     

while True:
    key = False

    img = cam.read()
    img = np.flip(img, axis=1)        #mirror camera
    img = np.array(img)

    hsv = cv2.cvtColor(img,cv2.COLOR_BGR2HSV) #color_ extract one colour that we need (hue saturation value)
    blurred = cv2.GaussianBlur(hsv,(11,11),0) #remove noise from image (extra data that we do not need) 

    colourLower = np.array([76,102, 151])       #HSV value
    colourUpper = np.array([180,255,255])     #HSV value
    '''using these hsv values you can filter out the excess 
    information to determine at what values i can filter out 
    the excessive information'''

    mask = cv2.inRange(blurred,colourLower,colourUpper)
    mask = cv2.morphologyEx(mask, cv2.MORPH_OPEN,np.ones((5,5),np.uint8))  #replace pixel with max value
    mask = cv2.morphologyEx(mask, cv2.MORPH_CLOSE,np.ones((5,5),np.uint8))
    width = img.shape[1]
    height = img.shape[0]

    upContour = mask[0:height//2,0:width]                           #upper part (left and right)
    downContour = mask[3*height//4:height,2*width//5:3*width//5]    #lower part (center for nitro)

    cnts_up = cv2.findContours(upContour,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts_up = imutils.grab_contours(cnts_up) #boundary

    cnts_down = cv2.findContours(downContour,cv2.RETR_EXTERNAL,cv2.CHAIN_APPROX_SIMPLE)
    cnts_down = imutils.grab_contours(cnts_down) #boundary
 
    if len(cnts_up) > 0: #boundary
        c = max(cnts_up,key = cv2.contourArea)
        M = cv2.moments(c)
        cX = int(M["m10"]/M["m00"]) #finds the centroid of rectangle(to know the left and right part is working or not !!)

        if cX < (width//2 -35):
            PressKey(D)         #keyboard key
            key=True
            currentKey.append(D)
        
        elif cX > (width//2 +35):
            PressKey(A)         #keyboard key
            key=True
            currentKey.append(A)
    
    # if len(cnts_down) > 0:
    # PressKey(W)
    # key = True
    # currentKey.append(W)

    img = cv2.rectangle(img, (0,0),(width//2-35,height//2),(0,255,0),1)
    # cv2.putText(img,'LEFT',(110,30),cv2.FONT_HERSHEY_DUPLEX, 1, (139,0,0))

    img = cv2.rectangle(img, (width//2+35,0),(width,height//2),(0,255,0),1)
    # cv2.putText(img,'RIGHT',(440,30),cv2.FONT_HERSHEY_DUPLEX,  1, (139,0,0))
 
    # img = cv2.rectangle(img, (2*(width//5),3*height//4),(3*width//5,height),(0,255,0),1)
    # cv2.putText(img,'NITRO',(2*(width//5) + 20,height-10),cv2.FONT_HERSHEY_DUPLEX,  1, (139,0,0))

    cv2.imshow("Steering", img)

    if not key and len(currentKey)!=0:
        for current in currentKey:
            ReleaseKey(current)

    key = cv2.waitKey(1) & 0xFF
    if key == ord('q'):
        break

cv2.destroyAllWindows()


