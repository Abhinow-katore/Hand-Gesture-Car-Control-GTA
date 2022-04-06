# **OPCRSN** - 
### Open-Convert-Remove-Search-Navigate
<a2 ><b>Open</b></a2> - Cv capture the image/stream. <br>
<b>Convert</b> - rgb to hsv, color_ extract one colour that we need (hue saturation value)<br>
<b>Remove</b> -  noise from image (extra data that we do not need) Gaussian blur to the hsv converted image.<br>
<b>Searching</b> - contours<br>
<b>Navigate</b> - the car.<br>

### Keys: file Source- directkey.py <br>
![image](https://user-images.githubusercontent.com/67780238/161909396-d8182ac0-fd05-4706-aa31-c2e566209e68.png)

**'''Feeding Key Presses to Reluctant Games in Python'''<br>
 Concept Source:**
 https://danieldusek.com/feeding-key-presses-to-reluctant-games-in-python.html
 
 It mimics the hardware input of the keyboard this also helps you bypass that some games they have bot detection mechanisms when you're playing online games they detect if the keystrokes are coming from the keyboard or from external third-party software
scancode
'''A scancode (or scan code) is the data that most
computer keyboards send to a computer to
report which keys have been pressed. A number,
 or sequence of numbers, is assigned to each key
 on the keyboard.''' 
 ### Source : https://gist.github.com/tracend/912308
<br>

## Mirroring camera
![image](https://user-images.githubusercontent.com/67780238/161907834-a9b1af44-0cce-468b-8305-02c2ba4eb583.png) 
<br>
## RGB to HSV <br>
![image](https://user-images.githubusercontent.com/67780238/161907916-b4d646b6-f135-4a5a-8097-eb0f7c446a16.png)
<br>
Using these hsv values you can filter out the excess information to determine at what values u can filter out the excessive information
    
![image](https://user-images.githubusercontent.com/67780238/161908013-f7fd3572-cfc4-49c3-85c8-e2b00a4b7f62.png)

![image](https://user-images.githubusercontent.com/67780238/161908192-1dea49d8-6f1c-46c9-8768-fb1d03833953.png)


## Gaussian Blurring
**Source**: https://docs.opencv.org/3.4/d4/d13/tutorial_py_filtering.html

![image](https://user-images.githubusercontent.com/67780238/161908409-68d5ce48-682c-417d-9422-e3362f4e7b34.png)
<br>
![image](https://user-images.githubusercontent.com/67780238/161908445-5d993f6b-e2b9-4ad0-b048-f8b58ffb14fc.png)
<br>
remove noise from image (extra data that we do not need)
<br>
## Dilation
<br>
We expand the image. It adds the number of pixels to the boundaries of objects in an image. The structuring element controls it. The structuring element is a matrix of 1's and 0's. <br>
<br>
First erodes the image and then dilates it morph close dilates the image and then erodes it what is meant by dilation and erosion let us check this <br>
**link out here** 
https://docs.google.com/document/d/1N66HRqW84DeWADsCFEmZFbXygHbYH-yxEC8WIuge4kc/edit# <br>
**This java** point article explains it very well filtering out excessive information and then erosion is the reverse of dilation what dilation does is it calculates the maximum value of pixels in a neighborhood and then switches the pixels 
<br>

##Find contours 
**Find contours method**
will look in this area for the colors, draw a boundary and return,all the points on the boundary 
<br>
![image](https://user-images.githubusercontent.com/67780238/161908742-b556073b-f8c8-48d7-a29e-69b70d45251a.png)
<br>
![image](https://user-images.githubusercontent.com/67780238/161908789-c7b81e28-e601-4c61-ad46-5b4d6e78d095.png)


     
