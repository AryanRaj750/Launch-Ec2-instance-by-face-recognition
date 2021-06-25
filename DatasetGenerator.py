#!/usr/bin/env python
# coding: utf-8

# In[1]:


import cv2, os
def faceExtractor(frame, FaceRecognizer):
    """ This function is for extracing the face from image. It helps to minimize the size of image and processing time
    for model training. 
    It takes two arguments frame read by camera and haarCasCadeFile.
    Example:- facaeExtractor(img, "harcasecade.xml")
    """
    faceRecognizer = cv2.CascadeClassifier(FaceRecognizer)
    grey = cv2.cvtColor(frame, cv2.COLOR_BGR2GRAY) # //This will change color frame into black&white for converting 3D into 2D.
    faces = faceRecognizer.detectMultiScale(grey, 1.3, 5)  # //It helps in pixels selection of face.
    if faces is ():
        return None

    for (x,y,w,h) in faces:
        cropped_face = frame[y:y+h, x:x+w] # // This is for face pixels array values

    return cropped_face

def generateDataset(ImageName, path="", FaceRecognizer="", ID=0, camera=0,numberOfImages=100):
    """ This is for generating new Datasets for Train-images. 
    It takes three arguments .g Name of image, path of image, and ID for image.
    Example:- generateDataset("aryan", "./train-imgages/", ID=3)
    camera = "http://192.165.43.3:8080/video" for Ip Camera.
    If you want to use IP camera then change camera value with IP. For example
    is given.
    """
    count = 0
    cap = cv2.VideoCapture(camera) # //It will provide connectivity with webcam/IpCamera to your program
    while cap.isOpened(): # // here, cheking camera is till now open or not, if opened then it return True as value.
        ret, frame = cap.read()  # //reding camera frame or capturing the images
        cface = faceExtractor(frame, FaceRecognizer) # //calling faceExtractor function for extracing the face from image. cface == croppedFace
        if cface is not None:
            count += 1
            face = cv2.resize(cface, (200, 200)) # resizing all images of same size e.g of 200x200(height and weight)
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY) #changing color image to grey to minimize training processing time
            fileNamePath = f"{path}{ImageName}/{ImageName}.{ID}." +str(count) + ".jpg" # //formating image file name
            cv2.imwrite(fileNamePath, face)  # //saving image to local storage
            cv2.putText(face, str(count), (50,50), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2) # //displaying count value on image
            cv2.imshow("face cropper", face) # // Displaying image to screen
        else:
            print("face not found")
            pass
        if cv2.waitKey(13) ==13 or count ==numberOfImages:
            break
    cap.release()
    cv2.destroyAllWindows()
    print("Collections completed!!!")


# In[3]:


#generateDataset("sohan", path="", FaceRecognizer="haarcascade_frontalface_default.xml", ID=0, camera=0)


# In[ ]:




