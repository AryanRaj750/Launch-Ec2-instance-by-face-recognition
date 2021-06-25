from  DatasetGenerator import generateDataset
from face_recognizer import FaceRecognizer
from modelTrain import trainModel
   
generateDataset("aryan", "./TrainImage/", "haarcascade_frontalface_default.xml",2) 
model = trainModel("./TrainImage/aryan/", 'aryan') 
NamesList = ['none', 'none', 'Aryan', 'Kundan']
models = ['./models/aryan.yml', './models/kundan.yml']
FaceRecognizer(models, NamesList, "haarcascade_frontalface_default.xml")
