import cv2, os
import numpy as np
from os import listdir
from os.path import isfile, join

def trainModel(dataPath, modelName):
    """ This function will help to traing model using LBPH (Local Binary pattern Hologram) algorithm.
    It will take one arguments e,g Image directory path 
    Image Name should be in format of 'Abc2.1jpg', here Abc is image Name, 2 is image ID, and 1 is for
    image count like image2.1.jpg, image2.2.jpg, image2.3.jpg etc
    """
    # onlyfiles will contain files name only like aryan1.jpg
    onlyfiles = [f for f in listdir(dataPath) if isfile(join(dataPath, f))]
    TrainingData, Labels = [], [] # //initialing two empty list for training data and labels/Id
    
    for file in onlyfiles:        # //iterating files name from onlyfiles list one by one
        imagePath = dataPath + file  #  //joining file name with path to get full path of image
        images = cv2.imread(imagePath, cv2.IMREAD_GRAYSCALE)   # // reading image providing file name
        TrainingData.append(np.asarray(images, dtype=np.uint8))  # // appending image array into trainingData array/list
        Id = int(os.path.split(imagePath)[-1].split(".")[1])     # //spliting Id name from image files
        Labels.append(Id)   # //appending labels into array/list

    Labels = np.asarray(Labels, dtype=np.int32)  # // chanign list int value into array with int32 type
    
    #model = cv2.face.LBPHFaceRecognizer_create()  
    model = cv2.face_LBPHFaceRecognizer.create()  # // creating empty model
    
    # //training model providing image array list and labels array list of int32 type
    model.train(np.asarray(TrainingData), np.asarray(Labels)) 
    
    #saving model to local storage
    model.save(f"./models/{modelName}.yml")
    
    # Displaying message for model trained
    print("model trained successfully")
    
    return model

#trainModel("./train-images/aryan/")