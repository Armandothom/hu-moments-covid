import os
import cv2
import numpy as np
from sklearn import preprocessing

def main():
    checkResultHuMoments()
    trainImagePath = './images_split/train/'
    testImagePath = './images_split/test/'
    trainFeaturePath = './features_labels/train/'
    testFeaturePath = './features_labels/test/'
    trainImages, trainLabels = getData(trainImagePath)
    trainEncodedLabels, encoderClasses = encodeLabels(trainLabels)
    trainFeatures = extractHuMoments(trainImages)
    saveData(trainFeaturePath,trainEncodedLabels,trainFeatures,encoderClasses)
    testImages, testLabels = getData(testImagePath)
    testEncodedLabels, encoderClasses = encodeLabels(testLabels)
    testFeatures = extractHuMoments(testImages)
    saveData(testFeaturePath,testEncodedLabels,testFeatures,encoderClasses)

def getData(path):
    images = []
    labels = []
    if os.path.exists(path):
        for dirpath , dirnames , filenames in os.walk(path):   
            if (len(filenames)>0): 
                folder_name = os.path.basename(dirpath)
                for index, file in enumerate(filenames):
                    label = folder_name
                    labels.append(label)
                    full_path = os.path.join(dirpath,file)
                    image = cv2.imread(full_path)
                    images.append(image)
        return images, np.array(labels,dtype=object)
    
def extractHuMoments(images):
    huMomentsImgs = []
    for image in images:
        if (np.ndim(image) > 2):
            image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
        ret, thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY)
        huMoments  = cv2.HuMoments(cv2.moments(thresh))
        huMomentsImgs.append(huMoments.flatten())
    return np.array(huMomentsImgs)

def checkResultHuMoments():
    test = []
    image = cv2.imread("diamond.png")
    if (np.ndim(image) > 2):
        image = cv2.cvtColor(image,cv2.COLOR_BGR2GRAY)
    ret, thresh = cv2.threshold(image, 0, 255, cv2.THRESH_BINARY)
    result = cv2.HuMoments(cv2.moments(image)).flatten()
    test.append(result)
    print(np.array(test))

def encodeLabels(labels):
    encoder = preprocessing.LabelEncoder()
    encoded_labels = encoder.fit_transform(labels)
    return np.array(encoded_labels,dtype=object), encoder.classes_

def saveData(path,labels,features,encoderClasses):
    label_filename = f'{labels=}'.split('=')[0]+'.csv'
    feature_filename = f'{features=}'.split('=')[0]+'.csv'
    encoder_filename = f'{encoderClasses=}'.split('=')[0]+'.csv'
    np.savetxt(path+label_filename,labels, delimiter=',',fmt='%i')
    np.savetxt(path+feature_filename,features, delimiter=',')
    np.savetxt(path+encoder_filename,encoderClasses, delimiter=',',fmt='%s') 

if __name__ == "__main__":
    main()
