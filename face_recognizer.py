from sendMail import sendMail, sendwhatmsg
import cv2, threading
import time, os
def faceDetector(img, detector, size=0.5):
    global x,y,w,h
    detector = cv2.CascadeClassifier(detector) # //using haarCasecade for face detection/boundary
    grey = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY) # // changing color image e.g 3D to black & white image e.g 2D
    faces = detector.detectMultiScale(grey, 1.3,5)  # //It will detect boundary for multi faces

    if faces is (): # //checking there is no any image without face
        return img, []  # //returning image without face

    for (x,y,w,h) in faces: # // x,y,w,h are face coordinates and width and height
        cv2.rectangle(img, (x,y), (x+w,y+h), (0,255,0), 2) # // drawing a rectangle boundary of green color
        roi = img[y:y+h, x:x+w]  # //cropping image of face size only, using coordinates value provided by haarCasecade
        roi = cv2.resize(roi, (200,200))  # //cropping each image of same size e.g 200x200(height and width)
        #pos = (x,y,w,h)

    return img, roi

def FaceRecognizer(modelFile, NamesList=[] , detector="haarcascade_frontalface_default.xml"):
    recognizer1 = cv2.face_LBPHFaceRecognizer.create()
    recognizer2 = cv2.face_LBPHFaceRecognizer.create() # initializing model object for prediction
    # recognizer = cv2.face.LBPHFaceRecognizer_create()
    recognizer1.read(modelFile[0]) # // it will read trained model, saved on local storage.
    recognizer2.read(modelFile[1]) # // it will read trained model, saved on local storage.
    count1 = 1
    count2 = 1
    count3 = 1
    cap = cv2.VideoCapture(0)
    #thread1 = threading.Thread(target=sendwhatmsg, args=("+917877205263", "testing for task6 summer program 2k21"))
    #thread2 = threading.Thread(target=sendMail, args=("mindedindia02@gmail.com", "Sa@230074","ar9131000@gmail.com", "testing for task6 summer program 2k21"))
                               
    while (cap.isOpened()):
        ret, image = cap.read() # //reading or capturing images        
        image, face = faceDetector(image, detector)
        #print(len(face))
        try:
            face = cv2.cvtColor(face, cv2.COLOR_BGR2GRAY) # // changing 3D array to 2D array, because model is trained in 2D

            Id1 ,results1 = recognizer1.predict(face) # //here, predict function will return two things e.g ID of image and
                                                   #connfidence score
            Id2 ,results2 = recognizer2.predict(face)
            label1 = NamesList[Id1]
            label2 = NamesList[Id2]
            if results1 < 500:
                confidence1 = int(100*(1-(results1)/400)) # // changing conf score into percentage
                displayString1 = str(confidence1) + "%"
                cv2.putText(image, displayString1, (x+20, y-20), cv2.FONT_HERSHEY_COMPLEX, 1, (219,41,97), 2)
                confidence2 = int(100*(1-(results2)/400)) # // changing conf score into percentage
                displayString2 = str(confidence2) + "%"
                cv2.putText(image, displayString2, (x+20, y-20), cv2.FONT_HERSHEY_COMPLEX, 1, (219,41,97), 2)
                
                if confidence1 >80:
                    cv2.putText(image, label1, (x+5, y + h+30), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
                    cv2.imshow("face Recognition", image)
                    if ( (count1 == 1) and (label1 == 'Aryan') ):    
                        sendwhatmsg("+917877205263", "testing for task6 summer program 2k21")
                        print("message sent to Guarav Jangid")
                        time.sleep(2)
                        count1 += 1
                        
                if confidence2 >80:
                    cv2.putText(image, label2, (x+5, y + h+30), cv2.FONT_HERSHEY_COMPLEX, 1, (0,255,0), 2)
                    cv2.imshow("face Recognition", image)
                    if ( (count2 == 1) and (label2 == 'Sonu') ):
                        sendMail("mindedindia02@gmail.com", "Sa@230074","ar9131000@gmail.com", "testing for task6 summer program 2k21")
                        print("mail sent to ar9131000@gmail.com")
                        time.sleep(2)
                        count2 += 1
                if ( (confidence1>80) and (confidence2>80) ):
                    if count3 == 1:
                        os.system("terraform init -auto-approve")
                        time.sleep(5)
                        os.system("terraform apply -auto-approve")
                        time.sleep(2)
                        print("ec2 instance launched, ebs volume created, and also attached....")
                        count3 += 1
                
            else:
                cv2.putText(image, "unknown user", (250,450), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
                cv2.imshow("face Recognition", image)

        except Exception as e:
            print(e)
            cv2.putText(image, "Face not detected", (220,120), cv2.FONT_HERSHEY_COMPLEX, 1, (0,0,255), 2)
            cv2.imshow("face Recognition", image)
            pass
        if cv2.waitKey(1) ==13:
            break
        
    cap.release()
    cv2.destroyAllWindows()

#names = ['none', 'none', 'Aryan', 'Kundan', 'Rajan', 'Ashok']
#FaceDetector("./models/aryan.yml", NamesList=names , FaceRecognizer="haarcascade_frontalface_default.xml")
