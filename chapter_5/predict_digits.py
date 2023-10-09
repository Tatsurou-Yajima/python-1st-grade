import sklearn.datasets
import sklearn.svm
import PIL.Image
import numpy as np
import os



def imageToData(filename):
    grayImage = PIL.Image.open(filename).convert("L")
    resizedGrayImage = grayImage.resize((8, 8), PIL.Image.Resampling.LANCZOS)
    numImage = np.asarray(resizedGrayImage, dtype=float)
    formattedNumImage = 16 - np.floor(17 * numImage / 256)
    return formattedNumImage.flatten()

def predictDigits(data):
    digits = sklearn.datasets.load_digits()
    clf = sklearn.svm.SVC(gamma=0.001)
    clf.fit(digits.data, digits.target)
    n = clf.predict([data])
    print("予測=", n)

data = imageToData("2.png")

predictDigits(data)
