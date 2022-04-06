 Keys
'''Feeding Key Presses to Reluctant Games in Python'''<br>
 Concept Source:
 https://danieldusek.com/feeding-key-presses-to-reluctant-games-in-python.html
 
 it mimics the hardware input of the keyboard this also helps you bypass that some games they have bot detection mechanisms when you're playing online games they detect if the keystrokes are coming from the keyboard or
 from external third-party software
scancode
'''A scancode (or scan code) is the data that most
computer keyboards send to a computer to
report which keys have been pressed. A number,
 or sequence of numbers, is assigned to each key
 on the keyboard.''' #source : https://gist.github.com/tracend/912308
 



#Mirroring camera;
![image](https://user-images.githubusercontent.com/67780238/161907834-a9b1af44-0cce-468b-8305-02c2ba4eb583.png)

#rgb to hsv
![image](https://user-images.githubusercontent.com/67780238/161907916-b4d646b6-f135-4a5a-8097-eb0f7c446a16.png)


'''using these hsv values you can filter out the excess 
    information to determine at what values u can filter out 
    the excessive information'''
    
![image](https://user-images.githubusercontent.com/67780238/161908013-f7fd3572-cfc4-49c3-85c8-e2b00a4b7f62.png)

![image](https://user-images.githubusercontent.com/67780238/161908192-1dea49d8-6f1c-46c9-8768-fb1d03833953.png)


#Gaussian Blurring
https://docs.opencv.org/3.4/d4/d13/tutorial_py_filtering.html

![image](https://user-images.githubusercontent.com/67780238/161908409-68d5ce48-682c-417d-9422-e3362f4e7b34.png)
![image](https://user-images.githubusercontent.com/67780238/161908445-5d993f6b-e2b9-4ad0-b048-f8b58ffb14fc.png)

remove noise from image (extra data that we do not need)
#Dilation
![image](https://user-images.githubusercontent.com/67780238/161908534-bdd4bb79-ca03-41e0-a271-eacf0fab4a52.png)


first erodes the image and then dilates it morph close dilates the image and then erodes it what is meant by dilation and erosion let us check this
link out here https://docs.google.com/document/d/1N66HRqW84DeWADsCFEmZFbXygHbYH-yxEC8WIuge4kc/edit#
this java d point uh article explains it very well filtering out excessive information and then erosion is the reverse of dilation what dilation does is it calculates the uh maximum value of pixels in a neighborhood and then switches the pixels 


#Find contours 
 find contours method
will look in this area for the colors, draw a boundary and return,all the points on the boundary 
![image](https://user-images.githubusercontent.com/67780238/161908742-b556073b-f8c8-48d7-a29e-69b70d45251a.png)
![image](https://user-images.githubusercontent.com/67780238/161908789-c7b81e28-e601-4c61-ad46-5b4d6e78d095.png)


     
