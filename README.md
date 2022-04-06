# Hand-Gesture-Car-Control-GTA
# Keys
'''Feeding Key Presses to Reluctant Games in Python'''
# Concept Source:
# https://danieldusek.com/feeding-key-presses-to-reluctant-games-in-python.html
 
# it mimics the hardware input of the keyboard this also helps you bypass that some games they have bot detection mechanisms when you're playing online games they detect if the keystrokes are coming from the keyboard or
# from external third-party software
#scancode
'''A scancode (or scan code) is the data that most
computer keyboards send to a computer to
report which keys have been pressed. A number,
 or sequence of numbers, is assigned to each key
 on the keyboard.''' #source : https://gist.github.com/tracend/912308
 



Mirroring camera;










2.rgb to hsv


#Convert rgb to hsv, color_ extract one colour that we need (hue saturation value)





'''using these hsv values you can filter out the excess 
    information to determine at what values i can filter out 
    the excessive information'''








Gaussian Blurring
https://docs.opencv.org/3.4/d4/d13/tutorial_py_filtering.html


remove noise from image (extra data that we do not need)






first erodes the image and then dilates it morph close
dilates the image and then erodes it
what is meant by
dilation and erosion let us check this
link out here https://docs.google.com/document/d/1N66HRqW84DeWADsCFEmZFbXygHbYH-yxEC8WIuge4kc/edit#
this java d point uh article explains it
very well
filtering out excessive information and
then erosion
is the reverse of dilation what dilation
does is it
calculates the uh maximum value of
pixels in a neighborhood
and then switches the pixels 


Find contours 
 find contours method
will look in this area for the colors, draw a boundary and return,all the points on the boundary 



     
